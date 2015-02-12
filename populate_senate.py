import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politician_tracker.settings')

import django
django.setup()

from profiles.models import Politician

import codecs
import requests
from bs4 import BeautifulSoup

# get raw data from requests.get and then put it into BS4 (adds tags)
raw_data = requests.get('https://en.wikipedia.org/wiki/List_of_current_United_States_Senators')
soup = BeautifulSoup(raw_data.text)
new_soup = soup.prettify()

with codecs.open("senate.json", "w", encoding="utf-8") as f:
	f.write(new_soup)

full_list = []
count = 0
# goes through each tr element (starting at the 21st to skip over other sections) inside the table and adds info to list in dictionaries
for index, row in enumerate(soup.find_all('tr')[21:121]):
	full_list.append([])
	full_list[index] = {}

	full_list[index]['district'] = row.contents[3].contents[0].contents[0].string
	full_list[index]['rank'] = row.contents[5].contents[0].string
	# full_list[index]['profile_pic_url'] = "https://en.wikipedia.org/" + str(row.contents[7].contents[0]['href'])[1:]  # wrong
	full_list[index]['wiki_url'] = "https://en.wikipedia.org" + row.contents[9].contents[1].a['href']
	full_list[index]['name'] = row.contents[9].contents[1].a.contents[0].string
	full_list[index]['party'] = row.contents[11].contents[0].string
	full_list[index]['chamber'] = u"U.S. Senate"
	full_list[index]['notes'] = ""



# loop to add each entry to database via the Politician model
for person in full_list:
	p = Politician(name=person['name'], wiki_url=person['wiki_url'], party=person['party'], district=person['district'], chamber=person['chamber'], notes=person['notes'], rank=person['rank'])
	p.save()
