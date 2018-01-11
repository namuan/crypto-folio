from .bittrex_exchange import BittrexExchange
from .gdax_exchange import GDaxExchange

bittrex = BittrexExchange()
gdax = GDaxExchange()

all_exchanges = [bittrex, gdax]
