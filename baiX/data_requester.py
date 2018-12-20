from urllib.request import urlopen
import json
from user import User

class DataRequester:
	url = 'https://jsonplaceholder.typicode.com/users'
	def __init__():
		pass
	@staticmethod
	def get_url_response():
		response = urlopen(url)
		string_result = response.read().decode('utf-8')
		json_objects = json.loads(string_result)
		return json_objects
