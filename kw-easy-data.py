#!/usr/bin/env python3

from pyfiglet import Figlet
import argparse
import requests
import json
from tabulate import tabulate
import csv

# print welcome message here with ascii art
f = Figlet(font='big')
print(f.renderText('KEYWORD EASY DATA'))
print("[i] Made by Federico De Faveri @ Keenn LLC", end="\n-----\n\n")

# get user-provided keyword and store it into a variable
parser = argparse.ArgumentParser(description='Get suggestions and search volume for a keyword')
parser.add_argument('-k', '--keyword', required=True, metavar='Keyword', help='The keyword that you want to get search data about')
parser.add_argument('-c', '--csv-out', required=False, metavar='Save as CSV', help='The file path where you want to save the results in csv format')

args = vars(parser.parse_args())
keyword = args['keyword']
csv_write_path = args['csv_out']

print(f'[*] Fetching related keywords and metrics for "{keyword}"...')

# shoot an API call to the backend service
base_url = 'https://seo-services.keenn.com/api'
api_method = '/get-kw-data'
payload = {
    'kw': keyword
}

full_url = f"{base_url}{api_method}"

response = requests.get(full_url, params=payload)

kw_data = response.json()['data']

# pretty print the results to Stdout
table_data = []
for kw_info in kw_data:
    individual_kw_data = {}
    individual_kw_data['keyword'] = kw_info['kw']
    individual_kw_data['search_vol_min'] = f"{kw_info['overall_monthly_volume']['volmin']}"
    individual_kw_data['search_vol_max'] = f"{kw_info['overall_monthly_volume']['volmax']}"
    individual_kw_data['cpc'] = kw_info['avg_cpc']
    table_data.append(individual_kw_data)

table_headers = ['KEYWORD', 'SEARCH VOLUME', 'CPC']

print()
print(tabulate(table_data, headers={'keyword': 'KEYWORD', 'search_vol_min': 'SEARCH VOLUME [MIN]','search_vol_max': 'SEARCH VOLUME [MAX]', 'cpc': 'AVG. CPC'}, tablefmt="grid"))
print()

# If csv flag exists save file to csv
if csv_write_path is not None:
    outfile = open(csv_write_path, 'w')
    writer = csv.DictWriter(outfile, fieldnames=['keyword', 'search_vol_min','search_vol_max', 'cpc'])
    writer.writeheader()
    writer.writerows(table_data)
    print(f"[*] File {csv_write_path} succesfully saved.")
    print()

exit(0)
