from kucoin.client import Client
from expiringdict import ExpiringDict

from config import env_cfg, log


class KucoinExchange:
    def __init__(self):
        self.disabled = False

        api_key = env_cfg("KUCOIN_KEY")
        api_secret = env_cfg('KUCOIN_SECRET')

        if api_key is None or api_secret is None:
            self.disabled = True
            log.info("Disable KUCOIN because either api_key or api_secret not available")
        else:
            self.client = Client(api_key, api_secret)
            self.cache = ExpiringDict(max_len=200, max_age_seconds=60)

    def is_disabled(self):
        return self.disabled

    def name(self):
        return self.__class__.__name__

    def get_balances(self):
        if self.disabled:
            raise EnvironmentError("{} is disabled".format(self.name()))

        if self.cache.get('balances'):
            return self.cache.get('balances')

        get_account_response = self.client.get_all_balances()

        balances = [
            {'exchange': 'KUCOIN', 'currency': b.get('coinType'), 'available': float(b.get('balance'))}
            for b in get_account_response
            if float(b.get('balance')) > 0
        ]

        self.cache['balances'] = balances
        return balances
