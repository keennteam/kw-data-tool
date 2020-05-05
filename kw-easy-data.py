#!/usr/local/bin/python3

import argparse
import requests
import json
from tabulate import tabulate

# get user-provided keyword and store it into a variable
parser = argparse.ArgumentParser(description='Get suggestions and search volume for a keyword')
parser.add_argument('-k', '--keyword', required=True, metavar='Keyword', help='The keyword that you want to get search data about')
parser.add_argument('-c', '--csv-out', required=False, metavar='Save as CSV', help='The file path where you want to save the results in csv format')

args = vars(parser.parse_args())
keyword = args['keyword']
csv_write_path = args['csv_out']

# print welcome message here with ascii art


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
    individual_kw_data = []
    individual_kw_data.append(kw_info['kw'])
    individual_kw_data.append(f"{kw_info['overall_monthly_volume']['volmin']} - {kw_info['overall_monthly_volume']['volmax']}")
    individual_kw_data.append(kw_info['avg_cpc'])
    table_data.append(individual_kw_data)

headers = ['KEYWORD', 'SEARCH VOLUME', 'CPC']

print()
print(tabulate(table_data, headers=headers, tablefmt="grid"))
print()

# If csv flag exists save to csv TODO
