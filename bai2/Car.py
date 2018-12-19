class Car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        print('Init a car')
    def run(self, kilometers):
        print('I ran '+str(kilometers))
