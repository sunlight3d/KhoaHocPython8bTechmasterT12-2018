class Car:
	def __init__(self, name, color, year):
		self.name = name
		self.color = color
		self.year = year
		print('Khoi tao tai Car')
	def to_string(self):
		return 'name ='+self.name+\
				',color='+self.color+\
				',year = '+str(self.year)

