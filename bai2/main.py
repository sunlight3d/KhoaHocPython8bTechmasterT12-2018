from Car import Car
from ElectricalCar import ElectricalCar

car1 = Car('Mazda X', 'red', 2019)
car1.run(100)
electrical_car1 = ElectricalCar('Tesla X', 'green', 2020, 300)
print(electrical_car1.name)