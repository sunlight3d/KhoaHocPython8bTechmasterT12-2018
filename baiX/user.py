class User:
	"""docstring for User"""
	def __init__(self, dictUser):
		super(User, self).__init__()		
		self.name = '' if dictUser['name'] is None else dictUser['name']
		self.email = '' if dictUser['name'] is None else dictUser['email']
		self.phone = '' if dictUser['name'] is None else dictUser['phone']
		self.website = '' if dictUser['name'] is None else dictUser['website']
	def to_string(self):
		return 'name: {}, email: {}, phone: {}, website: {}'.\
				format(self.name, self.email, self.phone, self.website)