import os, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politician_tracker.settings')

from pprint import pprint

import django
django.setup()

from profiles.models import Politician

json_data = open('congress_json.txt')
data = json.load(json_data)

for i in range(len(data)):

	birthday = data[i]['bio']['birthday']
	gender = data[i]['bio']['gender']
	religion = data[i]['bio'].get('religion')

	first = data[i]['name']['first']
	last = data[i]['name']['last']
	full_name = data[i]['name']['official_full']

	address = data[i]['terms'][-1]['address']
	office = data[i]['terms'][-1]['office']
	contact_form = data[i]['terms'][-1].get('contact_form')
	phone = data[i]['terms'][-1]['phone']

	id_bioguide = data[i]['id']['bioguide']
	id_govtrack = data[i]['id']['govtrack']

	party = data[i]['terms'][-1]['party']
	state = data[i]['terms'][-1]['state']
	chamber = data[i]['terms'][-1]['type']
	url = data[i]['terms'][-1]['url']
	rss_url = data[i]['terms'][-1].get('rss_url')
	term_end_date = data[i]['terms'][-1]['end']

	rep_district = data[i]['terms'][-1].get('district')
	sen_class =data[i]['terms'][-1].get('class')

	if data[i].get('leadership_roles'):
		role_start = data[i]['leadership_roles'][-1]['start']
		role_title = data[i]['leadership_roles'][-1]['title']
	else:
		role_start = None
		role_title = None

	p = Politician( first_name=first,
					last_name=last,
					official_full_name=full_name,
					birthday=birthday,
					gender=gender,
					religion=religion,
					address=address,
					office=office,
					contact_form=contact_form,
					phone=phone,
					id_bioguide=id_bioguide,
					id_govtrack=id_govtrack,
					party=party,
					state=state,
					chamber=chamber,
					url=url,
					rss_url=rss_url,
					term_end=term_end_date,
					rep_district=rep_district,
					sen_class=sen_class,
					role=role_title,
					role_start=role_start)

	p.save()
