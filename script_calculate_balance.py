#!/usr/bin/env python3
"""
Calculates total balance on multiple crypto exchanges and converts to the given currency

python3.6 script_calculate_balance.py

Setup as cron
0 */12 * * * python script_calculate_balance.py) >/dev/null 2>&1

"""
import argparse
import json
from itertools import groupby, chain
from operator import itemgetter
from config import *
from crypto_compare import CryptoCompare
from exchanges import all_exchanges

cc = CryptoCompare()


def load_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.loads(json_file.read())


def convert_currency(currency, available, rates):
    currency_rate = rates.get(currency)
    return available / currency_rate


def calculate_value(f, crypto_rates):
    currency = f.get('currency')
    available = float(f.get('available'))
    converted_value = available

    if currency not in fiat_currencies():
        converted_value = convert_currency(currency, available, crypto_rates)

    return {
        'currency': currency,
        'available': available,
        'converted_value': converted_value
    }


def build_message(main_currency, total_account_value, data):
    return "{}: {:06.8f}, {}: {:06.2f}  ({:.2f}%)".format(
        data.get('currency'),
        data.get('available'),
        main_currency,
        data.get('converted_value'),
        data.get('converted_value') / total_account_value * 100
    )


def calculate_coin_values(crypto_rates, exchange_coins):
    return [
        calculate_value(coin, crypto_rates)
        for coin in exchange_coins
    ]


def main(args):
    main_currency = args.currency

    exchange_balances = list(chain.from_iterable([e.get_balances() for e in all_exchanges]))

    t_syms = list(set([e.get('currency') for e in exchange_balances]))
    crypto_rates = cc.exchange_rates(main_currency, ",".join(t_syms))

    by_exchange_fn = lambda o: o.get('exchange')

    exchanges_with_coins = {
        k: calculate_coin_values(crypto_rates, v) for k, v in groupby(exchange_balances, by_exchange_fn)
    }

    all_currencies_with_values = list(chain.from_iterable(exchanges_with_coins.values()))
    total_account_value = sum(
        map(itemgetter('converted_value'), all_currencies_with_values)
    )

    exchange_messages = []

    for ex, exchange_coins in exchanges_with_coins.items():
        total_fiat_in_exchange = sum(
            map(itemgetter('converted_value'), exchange_coins)
        )

        exchange_coins_summary = "\n".join([
            build_message(main_currency, total_account_value, data) for data in exchange_coins
        ])
        exchange_messages.append("🗓  {}\n{}\nTotal {}: {:06.2f}  ({:.2f}%)".format(
            ex,
            exchange_coins_summary,
            main_currency,
            total_fiat_in_exchange,
            total_fiat_in_exchange / total_account_value * 100
        ))

    combined_message = "\n".join(exchange_messages)

    print("{}\nTotal: {:06.2f}".format(
        combined_message,
        total_account_value
    ))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--currency', required=True, help='Conversion currency')
    args = parser.parse_args()
    main(args)
