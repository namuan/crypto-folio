## CryptoFolio

A simple crypto currency portfolio viewer across multiple exchanges. 

[![asciicast](https://asciinema.org/a/3gGtqx9A2YHo5VB7hFzcw4ZN7.png)](https://asciinema.org/a/3gGtqx9A2YHo5VB7hFzcw4ZN7) 

### Exchanges supported

* [GDAX](https://www.coinbase.com/join/59934bb507e57a00a92eef18)
* [Bittrex](https://bittrex.com) 
* [Binance](https://www.binance.com/?ref=11695267)
* [Kucoin](https://www.kucoin.com/#/?r=22xtd)

### Installation:

Make sure you are using Python 3.6. The script uses matplotlib so please have a look at this [Faq](https://matplotlib.org/faq/virtualenv_faq.html) 
if you are running python in a virtual environment.

Install python dependencies

```
pip install -r requirements.txt
```

### Configuration:

Copy or rename env.cfg.sample file env.cfg and set the appropriate values for exchange API keys

```
[ALL]
BTREX_KEY = xxxx
BTREX_SECRET = xxxx

GDAX_PASSPHRASE = xxxx
GDAX_KEY = xxxx
GDAX_SECRET = xxxx

BINANCE_KEY = xxxx
BINANCE_SECRET = xxxx

KUCOIN_KEY = xxxx
KUCOIN_SECRET = xxxx

FIAT_CURRENCIES = USD, GBP, EUR
```

See the following table to setup API keys for each exchange  

**IMPORTANT**  
Please make sure that you don't have withdrawal or transfer capabilities when generating API Keys

| Exchange |API Settings page |
|:---- |:---- |
| `Gdax` | https://www.gdax.com/settings/api |
| `Bittrex` | https://bittrex.com/Manage#sectionApi |  
| `Binance` | https://www.binance.com/userCenter/createApi.html |
| `Kucoin` | https://www.kucoin.com/#/user/setting/api |


### Usage

```
$ python script_calculate_balance.py -c EUR

🗓  BITTREX
BTC: 0.00200000, EUR: 022.89  (69.72%)
XRP: 2.00000000, EUR: 003.46  (10.54%)
Total EUR: 026.35  (80.26%)
🗓  GDAX
BTC: 0.00001000, EUR: 000.11  (0.35%)
EUR: 5.87000000, EUR: 005.87  (17.88%)
ETH: 0.00050000, EUR: 000.50  (1.52%)
Total EUR: 006.48  (19.74%)
Total: 032.83
```

Each line contains the following information
```
[Currency] [Number of coins] [FIAT] [Currency value in Fiat] (weight across the whole portfolio)
``` 

To plot pie chart along with the table

```
python script_calculate_balance.py -c EUR -p
```

### TODO
 
✅ Add binance support
✅ Pie chart for visualising portfolio
[ ] Portfolio rebalancing
 
### Thanks

[python-binance](https://github.com/sammchardy/python-binance)   
[python-bittrex](https://github.com/ericsomdahl/python-bittrex)   
[python-kucoin](https://github.com/sammchardy/python-kucoin)  

### Disclaimer:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.