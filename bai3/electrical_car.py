from car import Car
from battery import Battery
class ElectricalCar(Car):
	def __init__(self, name, color, year, charging_voltage, battery):
		Car.__init__(self, name, color, year)
		# super().__init__(self, name, color, year)
		# super(ElectricalCar, self).__init__(self, name, color, year)
		self.charging_voltage = charging_voltage
		self.battery = battery
		print('Khoi tao tai ElectricalCar')
	
	def to_string(self):
		return Car.to_string(self)+'charging_voltage = '+\
				str(self.charging_voltage) +\
				self.battery.to_string()