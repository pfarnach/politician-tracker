import os, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politician_tracker.settings')

from pprint import pprint

import django
django.setup()

from profiles.models import Politician

json_data = open('congress_json.txt')
data = json.load(json_data)

for i in range(len(data)):

	current_id = data[i]['id']['bioguide']

	pol = Politician.objects.get(id_bioguide=current_id)

	pol.id_lis = data[i]['id'].get('lis')
	pol.id_maplight = data[i]['id'].get('maplight')
	pol.id_opensecrets = data[i]['id'].get('opensecrets')
	pol.id_thomas = data[i]['id'].get('thomas')
	pol.id_votesmart = data[i]['id'].get('votesmart')
	# id_govtrack = data[i]['id']['govtrack']
	try:
		pol.id_fec = data[i]['id']['fec'][-1]
	except:
		pol.id_fec = None

	pol.save()