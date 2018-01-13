from .bittrex_exchange import BittrexExchange
from .gdax_exchange import GDaxExchange
from .binance_exchange import BinanceExchange

bittrex = BittrexExchange()
gdax = GDaxExchange()
binance = BinanceExchange()

all_exchanges = [bittrex, gdax, binance]
