class Car:
    def __init__(self, color, model): #inicializator
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f'car {self.model} is driving to {location}')

class Bus(Car):
    def __init__(self, color, model, number):  # inicializator
        super().__init__(color,model)
        self.number = number

    def drive_to_location(self, location):
        print(f'bus {self.model} driving to geeks')

    def test(self):
        print(f'bus {self.color}')


bus_40 = Bus('red', 'dsada')
bus_40.drive_to_location('kuda-to')