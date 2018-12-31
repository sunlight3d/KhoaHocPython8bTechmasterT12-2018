"""Save user's data to local disk"""
def save_user_to_disk(dict_user):
	self.login_file = "login.data"
	file_writer = open(self.login_file, 'wb')
	pickle.dump([dict_user.id,dict_user.email, dict_user.password], file_writer) 