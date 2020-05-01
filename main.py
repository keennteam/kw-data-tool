#!/usr/local/bin/python3

from googleads import adwords

adwords_client = adwords.AdWordsClient.LoadFromStorage("./googleads.yaml")

print("Hello keyword data tool!", adwords_client)
