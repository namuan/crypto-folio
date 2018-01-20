#!/usr/bin/env python3
"""
Calculates total balance on multiple crypto exchanges and converts to the given currency

python3.6 script_calculate_balance.py

Setup as cron
0 */12 * * * python script_calculate_balance.py) >/dev/null 2>&1

"""
import argparse
import json
from itertools import chain
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd

from config import *
from crypto_compare import CryptoCompare
from exchanges import all_exchanges

cc = CryptoCompare()


def load_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.loads(json_file.read())


def convert_currency(currency, available, rates):
    currency_rate = rates.get(currency)
    if not currency_rate:
        return 0.0

    return available / currency_rate


def calculate_value(coin_data, crypto_rates):
    currency = coin_data.get('currency')
    available = float(coin_data.get('available'))
    converted_value = available

    if currency not in fiat_currencies():
        converted_value = convert_currency(currency, available, crypto_rates)

    return {
        'exchange': coin_data.get('exchange'),
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


def exchanges_balance_data():
    exchange_balances = list(chain.from_iterable([e.get_balances() for e in all_exchanges]))
    return exchange_balances


def fetch_crypto_rates(main_currency, exchange_balances):
    t_syms = list(set([e.get('currency') for e in exchange_balances]))
    crypto_rates = cc.exchange_rates(main_currency, ",".join(t_syms))
    return crypto_rates


def build_portfolio(main_currency):
    exchange_balances = exchanges_balance_data()
    crypto_rates = fetch_crypto_rates(main_currency, exchange_balances)
    coin_with_fiat_values = [
        calculate_value(coin, crypto_rates)
        for coin in exchange_balances
    ]
    portfolio_df = pd.DataFrame.from_records(coin_with_fiat_values)
    return portfolio_df[portfolio_df['converted_value'] > 0.01]


def main(args):
    main_currency = args.currency

    portfolio_df = build_portfolio(main_currency)

    total_account_value = portfolio_df['converted_value'].sum()

    portfolio_df['percentage'] = portfolio_df['converted_value'] / total_account_value * 100

    group_by_currencies = portfolio_df \
        .groupby('currency') \
        .agg({'converted_value': sum, 'available': sum, 'percentage': sum, 'exchange': min})

    group_by_currencies.sort_values(
        'converted_value',
        ascending=False,
        inplace=True
    )

    print(tabulate(group_by_currencies, headers='keys', tablefmt='grid', numalign='right', floatfmt='.2f'))

    print("Total: {:06.2f}".format(
        total_account_value
    ))

    if args.plot:
        plt.pie(
            group_by_currencies['percentage'],
            labels=group_by_currencies.index,
            shadow=False,
            autopct='%1.1f%%'
        )

        plt.axis('equal')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--currency', required=True, help='Conversion currency')
    parser.add_argument('-p', '--plot', action="store_true", help='Plot pie chart')
    args = parser.parse_args()
    main(args)
