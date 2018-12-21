from data_requester import DataRequester
from user import User
from excel_manager import ExcelManager

dict_users = DataRequester.get_url_response()
users = list(map(lambda dict_user: User(dict_user), dict_users))
for user in users:
	print(user.to_string())
excel_manager = ExcelManager('Book1.xlsx')
excel_manager.fill_data_to_first_sheet(users)
