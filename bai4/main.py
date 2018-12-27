from data_requester import DataRequester
from user import User
from excel_manager import ExcelManager

data_requester = DataRequester()
dict_users = data_requester.get_url_response()
users = []
for dict_user in dict_users:
	print('dict_user = {}'.format(dict_user))
	user = User(dict_user)
	users.append(user)
for user in users:
	pass
excel_manager = ExcelManager('Book1.xlsx')
excel_manager.fill_data_to_first_sheet(users)
# print(DataRequester.get_url_response())

