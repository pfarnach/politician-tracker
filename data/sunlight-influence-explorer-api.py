from pprint import pprint
import requests

#
# Entities
#

# params = {'apikey': '4fac0490b5a7444b9aa4a01fda4f9809',
# 		  'search': 'Barack Obama',
# 		  'type': 'politician',
# 		  'page': 1,
# 		  'per_page': 50}

# base_url = "http://transparencydata.org/api/1.0/entities.json"

# # send request to Congress v3 API and return json
# request = requests.get(base_url, params=params).json()


# pprint(request)
# print "\n*******************\n"


####################################################################


#
# Aggregates
#

params = {'apikey': '4fac0490b5a7444b9aa4a01fda4f9809',
		  'cycle': '2012',
		  'page': 1,
		  'per_page': 50}

base_url = "http://transparencydata.com/api/1.0/aggregates/pols/top_1000.json"

# send request to Congress v3 API and return json
request = requests.get(base_url, params=params).json()


pprint(request)
print "\n*******************\n"