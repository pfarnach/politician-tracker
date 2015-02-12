import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politician_tracker.settings')

import django
django.setup()

from profiles.models import Politician

import requests
from bs4 import BeautifulSoup

# get raw data from requests.get and then put it into BS4 (adds tags)
raw_data = requests.get('https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives_by_seniority')
soup = BeautifulSoup(raw_data.text)

full_list = []
count = 0
# goes through each tr element inside the table and adds info to list in dictionaries
for index, row in enumerate(soup.table.find_all('tr')):
	full_list.append([])
	full_list[index] = {}

	# runs into exception with the header which doesn't contain same information as body of table
	try:
		print row.contents[3].contents[0]['href']
		print 'https://en.wikipedia.org' + str(row.contents[3].contents[0]['href'])
		count += 1
		if count > 10:
			break
		# full_list[index]['rank'] = row.contents[1].contents[0].string
		# full_list[index]['name'] = row.contents[3].contents[0].string
		# full_list[index]['party'] = row.contents[5].contents[0].string
		# full_list[index]['district'] = row.contents[7].contents[0].string
		# full_list[index]['chamber'] = u"U.S. House of Representatives"

		# Some entries have notes -- some of these notes have plain text and url that have to be added together, like "Chair: Oversight and Government Reform"
		# try:
		# 	full_list[index]['notes'] = row.contents[11].contents[0].string + row.contents[11].contents[1].string
		# except TypeError:
		# 	full_list[index]['notes'] = row.contents[11].contents[0].string
	except (AttributeError, IndexError, TypeError):
		pass  # because errors will pop up when looking at headers


# loop to add each entry to database via the Politician model
# for person in full_list:
# 	# runs into error with notes -- some don't exist so it turns up a key error
# 	try:
# 		p = Politician(name=person['name'], party=person['party'], district=person['district'], chamber=person['chamber'], notes=person['notes'], rank=person['rank'])
# 	except KeyError:
# 		p = Politician(name=person['name'], party=person['party'], district=person['district'], chamber=person['chamber'], notes="n/a", rank=person['rank'])
# 	p.save()