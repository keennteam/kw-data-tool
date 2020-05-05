#!/usr/local/bin/python3

import argparse
import requests
import json

# get user-provided keyword and store it into a variable
parser = argparse.ArgumentParser(description='Get suggestions and search volume for a keyword')
parser.add_argument('-k', '--keyword', required=True, metavar='Keyword', help='The keyword that you want to get search data about')

args = vars(parser.parse_args())
keyword = args['keyword']

# shoot an API call to the backend service
base_url = 'https://seo-services.keenn.com/api'
api_method = '/get-kw-data'
payload = {
    'kw': keyword
}

full_url = f"{base_url}{api_method}"

response = requests.get(full_url, params=payload)

kw_data = response.json()['data']

for kw_info in kw_data:
    print(kw_info)
