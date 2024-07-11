import base64
import hmac
import os

import httpx
import hashlib
import time

import orjson
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from .exceptions import BybitAPIException, BybitRequestException


class BaseClient:
    API_URL = "https://api.bybit.com/"
    # SECONDARY_API_URL = "https://api.bytick.com/"
    TEST_NET_API_URL = "https://api-testnet.bybit.com/"
    DEMO_NET_API_URL = "https://api-demo.bybit.com/"
    API_VERSION = "v5"

    REQUEST_TIMEOUT: float = 5

    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        receive_window: int = 5000,
        sign_style: str = "HMAC",
        api_secret_passphrase: bytes | None = None,
        alternative_net: str = "",
    ):
        """API Client constructor
        :param api_key: Api Key
        :param api_secret: Api Secret. For RSA sign style, it should be the path to the private key file
        :param receive_window: Receive Window
        :param sign_style: Sign Style. Default HMAC. Choices: ["HMAC", "RSA"]
        :param api_secret_passphrase: RSA (or other cryptography method) private key passphrase
        :param alternative_net: Alternative network. Default empty to use mainnet. Choices: "test", "demo"
        """
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.API_SECRET: RSAPrivateKey | str
        self.sign_style = sign_style
        if self.sign_style != "HMAC":
            with open(api_secret, "rb") as f:
                self.API_SECRET = load_pem_private_key(f.read(), password=api_secret_passphrase)
        else:
            self.API_SECRET = api_secret
        self.receive_window = receive_window
        if sign_style != "HMAC" and sign_style != "RSA":
            raise ValueError("Invalid sign style. Must be HMAC or RSA")
        self.sign_style = sign_style
        self.timestamp_offset = 0
        if alternative_net == "test":
            self.base = self.TEST_NET_API_URL
        elif alternative_net == "demo":
            self.base = self.DEMO_NET_API_URL
        else:
            self.base = self.API_URL
        self.base_url = self.base + self.API_VERSION + "/"
        self.session = httpx.AsyncClient(http2=True, base_url=self.base_url)

    def _get_headers(self, timestamp_milli: int, signed=False, timeout: int = None) -> dict:
        headers = {
            "X-BAPI-TIMESTAMP": str(timestamp_milli),
            "X-BAPI-RECV-WINDOW": str(self.receive_window),
        }
        if signed:
            headers["X-BAPI-API-KEY"] = self.API_KEY
        return headers

    def _create_api_uri(self, path: str) -> httpx.URL:
        return httpx.URL(os.path.join(self.base, self.API_VERSION, path))

    def _generate_signature(self, request: httpx.Request, timestamp_milli: int) -> str:
        if request.method == "GET":
            prepared_str = str(timestamp_milli) + self.API_KEY + str(self.receive_window) + str(request.url.params)
        else:
            prepared_str = (
                str(timestamp_milli) + self.API_KEY + str(self.receive_window) + request.content.decode("utf-8")
            )
        prepared_bytes = prepared_str.encode("utf-8")
        if self.sign_style == "HMAC":
            return hmac.new(self.API_SECRET.encode("utf-8"), prepared_bytes, hashlib.sha256).hexdigest()
        else:  # RSA
            signature = self.API_SECRET.sign(prepared_bytes, padding.PKCS1v15(), hashes.SHA256())
            return base64.b64encode(signature).decode()

    def _get_request(self, method, uri, signed: bool, **kwargs) -> httpx.Request:
        timestamp = int(time.time() * 1000 + self.timestamp_offset)
        headers = self._get_headers(timestamp, signed)
        if method.lower() == "get":
            req = self.session.build_request(method, uri, headers=headers, params=kwargs)
        else:
            req = self.session.build_request(method, uri, headers=headers, json=kwargs)
        if signed:
            req.headers["X-BAPI-SIGN"] = self._generate_signature(req, timestamp)
            req.headers["X-BAPI-SIGN-TYPE"] = "2"
        return req


class AsyncClient(BaseClient):
    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        receive_window: int = 5000,
        sign_style: str = "HMAC",
        api_secret_passphrase: bytes | None = None,
        alternative_net: str = "",
    ):
        super().__init__(api_key, api_secret, receive_window, sign_style, api_secret_passphrase, alternative_net)
        self.session: httpx.AsyncClient = httpx.AsyncClient(http2=True)

    @classmethod
    async def create(
        cls,
        api_key: str | None = None,
        api_secret: str | None = None,
        receive_window: int = 5000,
        sign_style: str = "HMAC",
        api_secret_passphrase: bytes | None = None,
        alternative_net: str = "",
    ) -> "AsyncClient":
        self = cls(api_key, api_secret, receive_window, sign_style, api_secret_passphrase, alternative_net)

        try:
            # calculate timestamp offset between local and coinex server
            res = await self.get_server_time()
            self.timestamp_offset = 1000 * (int(res["result"]["timeSecond"]) - int(time.time()))

            return self
        except Exception:
            # If ping throw an exception, the current self must be cleaned
            # else, we can receive an "asyncio:Unclosed client session"
            await self.close_connection()
            raise

    async def __aenter__(self):
        return self

    async def __aexit__(self, *excinfo):
        await self.session.aclose()

    async def close_connection(self):
        if self.session:
            assert self.session
            await self.session.aclose()

    async def _request(self, method, uri: httpx.URL, signed: bool, **kwargs):
        request: httpx.Request = self._get_request(method, uri, signed, **kwargs)
        response = await self.session.send(request)
        return await self._handle_response(response)

    @staticmethod
    async def _handle_response(response: httpx.Response):
        """Internal helper for handling API responses from the server.
        Raises the appropriate exceptions when necessary; otherwise, returns the
        response.
        """
        if response.is_error:
            raise BybitAPIException(response, response.status_code, response.text)
        try:
            return orjson.loads(response.text)
        except ValueError:
            raise BybitRequestException(f"Invalid Response: {response.text}")

    async def _request_api(self, method, path, signed=False, **kwargs):
        uri = self._create_api_uri(path)
        return await self._request(method, uri, signed, **kwargs)

    async def _get(self, path, signed=False, **kwargs):
        return await self._request_api("get", path, signed, **kwargs)

    async def _post(self, path, signed=False, **kwargs) -> dict:
        return await self._request_api("post", path, signed, **kwargs)

    async def _put(self, path, signed=False, **kwargs) -> dict:
        return await self._request_api("put", path, signed, **kwargs)

    async def _delete(self, path, signed=False, **kwargs) -> dict:
        return await self._request_api("delete", path, signed, **kwargs)

    async def get_server_time(self) -> dict:
        return await self._get("market/time")

    async def get_symbol_info(self, **kwargs) -> dict:
        return await self._get("market/instruments-info", **kwargs)

    async def get_orderbook(self, **kwargs) -> dict:
        return await self._get("market/orderbook", **kwargs)

    async def get_klines(self, **kwargs) -> dict:
        return await self._get("market/kline", **kwargs)

    async def get_funding_history(self, **kwargs) -> dict:
        return await self._get("market/funding/history", **kwargs)

    async def get_ticker(self, **kwargs) -> dict:
        return await self._get("market/tickers", **kwargs)

    async def place_order(self, **kwargs) -> dict:
        return await self._post("order/create", **kwargs, signed=True)

    async def amend_order(self, **kwargs) -> dict:
        return await self._post("order/amend", **kwargs, signed=True)

    async def cancel_order(self, **kwargs) -> dict:
        return await self._post("order/cancel", **kwargs, signed=True)

    async def cancel_all_orders(self, **kwargs) -> dict:
        return await self._post("order/cancel-all", **kwargs, signed=True)

    async def get_order_history(self, **kwargs) -> dict:
        return await self._get("order/history", **kwargs, signed=True)

    async def get_open_orders(self, **kwargs) -> dict:
        return await self._get("order/realtime", **kwargs, signed=True)

    async def get_execution_history(self, **kwargs) -> dict:
        return await self._get("execution/list", **kwargs, signed=True)

    async def get_position_info(self, **kwargs) -> dict:
        return await self._get("position/list", **kwargs, signed=True)

    async def set_leverage(self, **kwargs) -> dict:
        return await self._post("position/set-leverage", **kwargs, signed=True)

    async def get_wallet_balance(self, **kwargs) -> dict:
        return await self._get("account/wallet-balance", **kwargs, signed=True)

    async def set_collateral_switch(self, **kwargs) -> dict:
        return await self._post("account/set-collateral-switch", **kwargs, signed=True)

    async def get_borrow_history(self, **kwargs) -> dict:
        return await self._get("account/borrow-history", **kwargs, signed=True)

    async def get_collateral_info(self, **kwargs) -> dict:
        return await self._get("account/collateral-info", **kwargs, signed=True)

    async def get_fee_rate(self, **kwargs) -> dict:
        return await self._get("account/fee-rate", **kwargs, signed=True)

    async def get_transaction_log(self, **kwargs) -> dict:
        return await self._get("account/transaction-log", **kwargs, signed=True)

    async def get_account_info(self) -> dict:
        return await self._get("account/info", signed=True)

    async def set_hedging_mode(self, **kwargs) -> dict:
        return await self._post("account/set-hedging-mode", **kwargs, signed=True)

    async def get_coin_greeks(self, **kwargs) -> dict:
        return await self._get("asset/coin-greeks", **kwargs, signed=True)

    async def get_spot_margin_trade_data(self, **kwargs) -> dict:
        return await self._get("spot-margin-trade/data", **kwargs)

    async def switch_spot_margin_trade_mode(self, **kwargs) -> dict:
        return await self._post("spot-margin-trade/switch-mode", **kwargs, signed=True)

    async def set_spot_margin_trade_leverage(self, **kwargs) -> dict:
        return await self._post("spot-margin-trade/set-leverage", **kwargs, signed=True)

    async def get_spot_margin_trade_state(self, **kwargs) -> dict:
        return await self._get("spot-margin-trade/state", **kwargs, signed=True)

    async def create_universal_transfer(self, **kwargs) -> dict:
        return await self._post("asset/transfer/universal-transfer", **kwargs, signed=True)

    async def get_universal_transfer_records(self, **kwargs) -> dict:
        return await self._get("asset/transfer/query-universal-transfer-list", **kwargs, signed=True)
