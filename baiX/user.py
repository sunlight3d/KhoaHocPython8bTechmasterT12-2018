class User:
	"""docstring for User"""
	def __init__(self, dictUser):
		super(User, self).__init__()
		self.name = dictUser['name'] is None ? '' : dictUser['name']
		self.email = dictUser['email'] is None ? '' : dictUser['email']
		self.phone = dictUser['phone'] is None ? '' : dictUser['phone']
		self.website = dictUser['website'] is None ? '' dictUser['website']: 
	def __repl__(self):
		return 'name: {}, email: {}, phone: {}, website: {}'.\
				format(self.name, self.email, self.phone, self.website)