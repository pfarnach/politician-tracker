import os, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politician_tracker.settings')

from pprint import pprint
import requests

import django
django.setup()

from profiles.models import Politician

# json_data = open('congress-api-data.txt')
# data = json_data.read()

# print data[0:15]
count = 1

# loops through query database by page (max 50 entries per page, so have to go through at least 12 pages)
for i in range(1,13):

	# parameters for search
	params = {'apikey': '4fac0490b5a7444b9aa4a01fda4f9809',
			  'all_legislators': True,
			  'page': i,
			  'per_page': 50}

	base_url = "https://congress.api.sunlightfoundation.com/legislators"

	# send request to Congress v3 API and return json
	request = requests.get(base_url, params=params).json()

	# loop through each entry (politician) and pull
	for i in range(len(request['results'])):
		current_id = request['results'][i]['bioguide_id']
		pol = Politician.objects.get(id_bioguide=current_id)

		if not pol.twitter_id:
			try:
				pol.twitter_id = request['results'][i]['twitter_id']
				print "Twitter added for", pol.official_full_name
			except KeyError:
				print "No twitter for", pol.official_full_name

		if not pol.facebook_id:
			try:
				pol.facebook_id = request['results'][i]['facebook_id']
				print "Facebook added for", pol.official_full_name
			except KeyError:
				print "No facebook for", pol.official_full_name

		if not pol.youtube_id:
			try:
				pol.youtube_id = request['results'][i]['youtube_id']
				print "Youtube added for", pol.official_full_name
			except KeyError:
				print "No youtube for", pol.official_full_name

		print count
		print "\n**********************\n"
		pol.save()
		count += 1


# with open('congress-api-data.txt', 'a') as outfile:
# 	json.dump(complete, outfile, sort_keys = True, indent = 4)
