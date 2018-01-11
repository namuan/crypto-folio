### CryptoFolio

A simple crypto currency portfolio viewer across multiple exchanges. 

#### Installation:

Make sure you are using Python 3.6

Install python dependencies

```
pip install -r requirements.txt
```

#### Configuration:

Copy or rename env.cfg.sample file env.cfg and set the appropriate values for exchange API keys

```
[ALL]
BTREX_KEY = xxxx
BTREX_SECRET = xxxx

GDAX_PASSPHRASE = xxxx
GDAX_KEY = xxxx
GDAX_SECRET = xxxx

FIAT_CURRENCIES = USD, GBP, EUR
```

#### Application

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

##### Exchanges supported

GDAX 
Bittrex 

#### TODO

[ ] Add binance support  

#### Disclaimer:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.