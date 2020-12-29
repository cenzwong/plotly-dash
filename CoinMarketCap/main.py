# !curl -H "X-CMC_PRO_API_KEY: 92e361bb-c2cb-4520-8cdd-9ceb3b3b8ba5-cenz" -H "Accept: application/json" -d "start=1&limit=5000&convert=USD" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest

import requests

payload = {'symbol': 'BTC,ETH,MCO,PAXG',  'convert': 'USD'}
headers = {'X-CMC_PRO_API_KEY': '92e361bb-c2cb-4520-8cdd-9ceb3b3b8ba5'}
r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', params=payload, headers=headers)
json_coinmarketcap = r.json()

"""

{'BTC': {'circulating_supply': 18405493,
         'cmc_rank': 1,
         'date_added': '2013-04-28T00:00:00.000Z',
         'id': 1,
         'is_active': 1,
         'is_fiat': 0,
         'last_updated': '2020-06-15T15:03:31.000Z',
         'max_supply': 21000000,
         'name': 'Bitcoin',
         'num_market_pairs': 8393,
         'platform': None,
         'quote': {'USD': {'last_updated': '2020-06-15T15:03:31.000Z',
                           'market_cap': 169652016829.61172,
                           'percent_change_1h': 0.492039,
                           'percent_change_24h': -2.09483,
                           'percent_change_7d': -5.16399,
                           'price': 9217.46659161,
                           'volume_24h': 24320902380.8482}},
         'slug': 'bitcoin',
         'symbol': 'BTC',
         'tags': ['mineable'],
         'total_supply': 18405493},
 'ETH': {'circulating_supply': 111360275.8115,
         'cmc_rank': 2,
         'date_added': '2015-08-07T00:00:00.000Z',
         'id': 1027,
         'is_active': 1,
         'is_fiat': 0,
         'last_updated': '2020-06-15T15:03:33.000Z',
         'max_supply': None,
         'name': 'Ethereum',
         'num_market_pairs': 5177,
         'platform': None,
         'quote': {'USD': {'last_updated': '2020-06-15T15:03:33.000Z',
                           'market_cap': 25161080889.75299,
                           'percent_change_1h': 0.4514,
                           'percent_change_24h': -4.19635,
                           'percent_change_7d': -7.0998,
                           'price': 225.943054706,
                           'volume_24h': 9799465120.29494}},
         'slug': 'ethereum',
         'symbol': 'ETH',
         'tags': ['mineable'],
         'total_supply': 111360275.8115},}

"""
