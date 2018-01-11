from bittrex.bittrex import Bittrex, API_V1_1
from expiringdict import ExpiringDict

from config import env_cfg, log


class BittrexExchange:
    def __init__(self):
        self.disabled = False

        api_key = env_cfg("BTREX_KEY")
        api_secret = env_cfg('BTREX_SECRET')

        if api_key is None or api_secret is None:
            self.disabled = True
            log.info("Disable BITTREX because either api_key or api_secret not available")
        else:
            self.bittrex_v1 = Bittrex(api_key, api_secret, api_version=API_V1_1)
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

        get_balances_response = self.bittrex_v1.get_balances()

        balances = [
            {'exchange': 'BITTREX', 'currency': b.get('Currency'), 'available': b.get('Balance')}
            for b in self.result(get_balances_response)
            if b.get('Balance') > 0
        ]
        self.cache['balances'] = balances
        return balances

    @staticmethod
    def result(api_response):
        if api_response.get('success'):
            return api_response.get('result')

        raise ConnectionError("API Failed: {}".format(api_response))
