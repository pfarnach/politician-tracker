import requests, sys, pprint

class CongressAPI(object):

	def __init__(self, api_key, district, last_name = "None", first_name = "None"):
		self.api_key = api_key
		self.last_name = last_name.title()
		self.first_name = first_name.title()
		self.district = district

	def call_api(self):
		parameters = {
			'apikey': self.api_key,
			# 'per_page': 5,
			'last_name': self.last_name,
			# 'first_name': self.first_name,
			#'type': 'politician',

		}

		endpoint = 'https://congress.api.sunlightfoundation.com/legislators'

		response = requests.get(endpoint, params = parameters)
		data = response.json()
		pprint.pprint(data)
		# print data['results'][0]['youtube_id']


def main():
	# api = CongressAPI('4fac0490b5a7444b9aa4a01fda4f9809', sys.argv[1], sys.argv[2])
	api = CongressAPI('4fac0490b5a7444b9aa4a01fda4f9809', sys.argv[1])
	api.call_api()

if __name__ == "__main__":
	main()


data[0]['name']['last']