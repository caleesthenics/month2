# class Car:
#
#     def __init__(self, color, model): #inicializator
#         self.color = color
#         self.model = model
#         self._fined = False #защищенный атрибут
#         self.__testt = False #приватный атрибут (можно юзать только внутри класса,на классы приемники не распростроняется)
#
#     def drive_to_location(self,location ):
#         print(f'Car {self.model} is driving to {location}')
#
#     def _test_car(self):
#         print('test') #защищенный метод
#
#     def get_test(self):
#         return self.__testt #getter
#
#     def set_test(self, testt):
#         self.__testt = testt #setter
#
# class Bus(Car):
#     def test_bus(self):
#         print(f'test bus {self.get_test()}')
#
# bus_40 = Bus('green', '400')
#
# bus_40.test_bus()
#
# @property (getter toje)
#
# @(metod).setter  (setter toje)
#
# car_honda = Car('black', 'honda_civic')
#
# car_honda.set_test(True)
#
# print(car_honda.get_test())
#
# print(car_honda._Car__testt) #для того,чтобы посмотреть приватный атрибут (name mangling)
#
# car_honda.color = 'greengig'
#
# print(car_honda.color)
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):      #абстракция (используется как шаблон для других классов,в нём ничего не реализуется)
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print('sobaka laet')
#
# dog = Dog()
#
# dog.make_sound()