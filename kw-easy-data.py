#!/usr/local/bin/python3

import argparse
import requests
import json

# get keywords
parser = argparse.ArgumentParser(description='Get suggestions and search volume for a keyword')
parser.add_argument('-k', '--keyword', required=True, metavar='Keyword', help='The keyword that you want to get search data about')

args = vars(parser.parse_args())

print(args)
