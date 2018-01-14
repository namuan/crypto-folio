from .bittrex_exchange import BittrexExchange
from .gdax_exchange import GDaxExchange
from .binance_exchange import BinanceExchange
from .kucoin_exchange import KucoinExchange

bittrex = BittrexExchange()
gdax = GDaxExchange()
binance = BinanceExchange()
kucoin = KucoinExchange()

all_exchanges = [bittrex, gdax, binance, kucoin]
