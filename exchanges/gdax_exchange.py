import gdax

from config import env_cfg, log
from expiringdict import ExpiringDict


class GDaxExchange:
    def __init__(self):
        self.disabled = False

        pass_phrase = env_cfg("GDAX_PASSPHRASE")
        key = env_cfg("GDAX_KEY")
        secret = env_cfg("GDAX_SECRET")

        if pass_phrase is None or key is None or secret is None:
            self.disabled = True
            log.info("Disable GDAX because either api_key or api_secret not available")
        else:
            self.client = gdax.AuthenticatedClient(key, secret, pass_phrase)
            self.cache = ExpiringDict(max_len=200, max_age_seconds=60)

    def name(self):
        return self.__class__.__name__

    def get_balances(self):
        if self.disabled:
            raise EnvironmentError("{} is disabled".format(self.name()))

        if self.cache.get('balances'):
            return self.cache.get('balances')

        get_accounts = self.client.get_accounts()

        balances = [
            {'exchange': 'GDAX', 'currency': b.get('currency'), 'available': b.get('available')}
            for b in get_accounts
            if float(b.get('available')) > 0
        ]

        self.cache['balances'] = balances
        return balances
