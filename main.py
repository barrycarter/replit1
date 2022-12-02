"""
Docstring
Fill this out later.
"""


import csv
from collections import namedtuple
from collections import OrderedDict
import argparse
import requests


print('\n' + 'step1-API')  # TEMP to see progress in script
# Temp API made for Reddit post.
response = requests.get('https://cloud.iexapis.com/stable/tops/last?token='
                        'pk_82c2dab6b26d4a50bd7e86e2800156c3&'
                        'symbols=SNAP,AMZN,AAPL', timeout=30)
print(response.content)  # TEMP to see progress in script

print('\n' + 'step2-Import')  # TEMPORARY
with open('portfolio.csv', newline='', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(*row, sep='\t')

# imported_symbol = ?
# imported_units = ?
# imported_cost = ?

print('\n' + 'step3-Export')  # TEMP to see progress in script
with open('portfolio_output.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(['symbol', 'units', 'cost', 'latest_price', 'book_value',
                     'market_value', 'gain_loss', 'change'])

print('\n' + 'step4-Nice_Export')  # TEMP to see progress in script
Performance = namedtuple('Performance', ['symbol', 'units', 'cost', 'latest_price',
                                         'book_value', 'market_value', 'gain_loss', 'change'])

with open('portfolio_output.csv', newline='', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        performance = Performance(*row)
        report = f'Closed at ${performance.latest_price} on {performance.change}'
        print(report)

print('\n' + 'End')  # TEMP to see progress in script
