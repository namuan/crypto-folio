import requests
from expiringdict import ExpiringDict

from config import log

BASE_URL = "https://min-api.cryptocompare.com"


class CryptoCompare:
    def __init__(self):
        self.cache = ExpiringDict(max_len=200, max_age_seconds=60)

    def exchange_rates(self, from_sym, to_syms):
        key = "rates_data_{}_{}".format(from_sym, to_syms.replace(",", ""))
        if self.cache.get(key):
            return self.cache.get(key)

        url = "{}/data/price?fsym={}&tsyms={}".format(
            BASE_URL,
            from_sym,
            to_syms
        )
        log.info("Getting exchange rates via: {}".format(url))

        crypto_exchange_data = requests.get(url).json()

        self.cache[key] = crypto_exchange_data

        return crypto_exchange_data
