from data_requester import DataRequester
from user import User

dict_users = DataRequester.get_url_response()
users = list(map(lambda dict_user: User(dict_user), dict_users))
for user in users:
	print(str(user))