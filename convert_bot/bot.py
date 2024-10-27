from BybitClient.BybitClient import BybitClient

API_KEY = 'gxzATNShNS96F3dFCd'  # реальный
API_SECRET = 'OKBL1LLBbpPrgbvDm0bMmhSROCbtpD5oNDpd' # реальный


class Bot:
    def __init__(self, api_key: str = API_KEY, api_secret: str = API_SECRET, testnet: bool = False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.client = self._create_client()

    def _create_client(self):
        return BybitClient(testnet=self.testnet, api_key=self.api_key, api_secret=self.api_secret, log_requests=True)

    def get_balance(self, coin: str = "BTC"):
        """Получить баланс для указанной валюты."""
        response = self.client.get_wallet_balance(accountType='UNIFIED', coin=coin)
        return response

    def place_order(self, symbol: str, side: str, order_type: str, qty: float, price: float = None,
                    time_in_force: str = "GoodTillCancel"):
        """Разместить ордер на покупку или продажу."""
        order = self.client.place_active_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            qty=qty,
            price=price,
            time_in_force=time_in_force
        )
        return order

    def get_trading_pairs(self, category: str = 'linear'):
        """Получить список всех доступных валютных пар."""
        symbols_info = self.client.get_instruments_info(category=category)
        return [symbol['symbol'] for symbol in symbols_info['result']['list']]