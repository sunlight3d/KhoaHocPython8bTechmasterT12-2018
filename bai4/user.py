class User:
	"""docstring for User"""
	def __init__(self, dictUser):
		super(User, self).__init__()	
		if dictUser['name'] is None:
			self.name = ''
		else:
			self.name = dictUser['name']
			
		self.email = '' if dictUser['email'] is None else dictUser['email']
		self.phone = '' if dictUser['phone'] is None else dictUser['phone']
		self.website = '' if dictUser['website'] is None else dictUser['website']
	def to_string(self):
		return 'name: {}, email: {}, phone: {}, website: {}'.\
				format(self.name, self.email, self.phone, self.website)