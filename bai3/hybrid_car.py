from electrical_car import ElectricalCar
from gasoline_car import GasolineCar
class HybridCar(ElectricalCar, GasolineCar):
	def __init__(self, ame, color, year, charging_voltage, volume):		
		Car.__init__(self, name, color, year)	
		self.charging_voltage = charging_voltage
		self.volume = volume
		print('Khoi tao Battery')
	
	def to_string(self):
		return 'name = {}, year={}, warranty={}'.\
				format(self.name, self.year, self.warranty)