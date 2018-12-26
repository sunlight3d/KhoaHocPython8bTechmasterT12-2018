from urllib.request import urlopen
import json
from urls import *
class DataRequester:
    # url = 'https://jsonplaceholder.typicode.com/users'
    def __init__(self):
        pass
    def get_url_response(self):
        response = urlopen(url_get_users)
        string_result = response.read().decode('utf-8')
        json_objects = json.loads(string_result)
        return json_objects
		