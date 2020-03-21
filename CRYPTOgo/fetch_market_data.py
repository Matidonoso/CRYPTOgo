#https://github.com/Vanclief/algo-trading-crypto/blob/master/scripts/fetch_market_data.py

import requests
import argparse
import pandas as pd

def get_historical_hourly_price(
        symbol,
        comparison_symbol,
        limit,
        aggregate,
        exchange=''):
    """
    Get the historical OHCL of a certain symbol pair for a certain
    exchange
    """
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)

    if exchange:
        url += '&e={}'.format(exchange)

    page = requests.get(url)
    data = page.json()['Data']
    data_frame = pd.DataFrame(data)
    data_frame['mid'] = data_frame[["high", "low"]].mean(axis=1)
    data_frame = data_frame.set_index('time')

    return data_frame