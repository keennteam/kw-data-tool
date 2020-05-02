#!/usr/local/bin/python3

from googleads import adwords

adwords_client = adwords.AdWordsClient.LoadFromStorage("./googleads.yaml")

targeting_idea_service = adwords_client.GetService('TargetingIdeaService')

selector = {
    'ideaType': 'KEYWORD',
    'requestType': 'IDEAS'
}

selector['searchParameters'] = [{
    'xsi_type': 'RelatedToQuerySearchParameter',
    'queries': ['space cruise']
}]

offset = 0
selector['paging'] = {
    'startIndex': str(offset),
    'numberResults': str(5)
}

page = targeting_idea_service.get(selector)
