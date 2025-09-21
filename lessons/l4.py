class Animal:
    def speak(self):
        print('animal')

class Cat(Animal):
    def speak(self):
        print('meow')

class Dog(Animal):
    def speak(self):
        print('gav')

class CatDog(Cat, Dog):
    def speak(self):
        print('alo')

kotopes = CatDog()

kotopes.speak() #будет обращаться к методу speak по очереди(от своего класса до класса родителя), Diamond Problem

# print(CatDog.__mro__) #method resolution order
#метод super цепляется к следующему в цепочке mro классу