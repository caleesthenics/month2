class Car:
    def __init__(self, color, model): #inicializator
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f'car {self.model} is driving to {location}')

car_honda = Car('silver', 'honda')

car_subaru = Car('black', 'subaru')

car_subaru.drive_to_location('bishkek')

print(car_subaru)

print(f"car olor {car_subaru.color},model {car_subaru.model}")

car_honda.color = 'red'



# print(type(car_honda))

# git config --global user.name "Albert Lee"
# git config --global user.email koresaremi2001@gmail.co