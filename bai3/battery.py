class Battery:
	def __init__(self, name, year, warranty):		
		self.name = name
		self.year = year
		self.warranty = warranty		
		print('Khoi tao Battery')
	
	def to_string(self):
		return 'name = {}, year={}, warranty={}'.\
				format(self.name, self.year, self.warranty)