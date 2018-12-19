from Car import Car
class ElectricalCar(Car):
    def __init__(self, name, color, year, charging_voltage):
        # super(ElectricalCar, self).__init__(name, color, year)
        self.charging_voltage = charging_voltage