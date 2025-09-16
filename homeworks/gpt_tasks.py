# 🔹 Задача 1: Банковский счёт (уровень: лёгкий)
# Условие:
# Создай класс BankAccount, который будет моделировать банковский счёт.
# Требования:
# При инициализации счёт должен иметь имя владельца и начальный баланс (по умолчанию 0).
# Методы:
# deposit(amount) – пополнить счёт.
# withdraw(amount) – снять со счёта (если хватает средств).
# get_balance() – вернуть текущий баланс.

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        print(self.balance)

account = BankAccount("Petya", 200)
account.deposit(1000)
account.withdraw(2000)

account.get_balance()


# 🔹 Задача 2: Управление зоопарком (уровень: средний)
# Условие:
# Сделай систему классов для зоопарка. У тебя есть базовый класс Animal и производные классы Lion, Elephant, Monkey.
# Требования:
# Класс Animal должен иметь:
# имя (name)
# возраст (age)
# метод make_sound() (абстрактный — в базовом классе ничего не делает)
# У каждого подкласса должен быть свой звук в make_sound().
# Сделай класс Zoo, который хранит список животных и умеет:
# добавлять животных
# показывать список всех животных
# вызывать make_sound() у каждого животного


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print('RRRR')


class Elephant(Animal):
    def make_sound(self):
        print('hzz')

class Monkey(Animal):
    def make_sound(self):
        print('uu aa')

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal.name)

    def sound(self):
        for animal in self.animals:
            animal.make_sound()

lev = Lion('hz', 23,)

slon = Elephant('SLON', 21)

martishka = Monkey('Monkeyy', 2)

zoo = Zoo()
zoo.add_animal(slon)
zoo.add_animal(martishka)
zoo.add_animal(lev)
zoo.sound()
zoo.show_animals()

# Симулировать школьный журнал с учениками разных ролей: обычный ученик, отличник, двоечник. Создай систему, где можно добавлять учеников, выводить их список и вызывать их действия (например, как они учатся).
# 🔧 Условие:
# Абстрактный класс Student:
# Поля: name, age
# Абстрактный метод study() — поведение при учебе
# Подлассы:
# ExcellentStudent — говорит "Учусь на отлично!"
# BadStudent — говорит "Опять двойка..."
# AverageStudent — говорит "Ну, нормально вроде..."
# Класс SchoolJournal:
# Хранит список учеников
# Методы:
# add_student(student) — добавляет ученика, если он экземпляр Student
# show_students() — показывает список всех учеников с их типами
# students_study() — вызывает метод study() у каждого

class Student(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def study(self):
        pass

class ExcellentStudent(Student):
    def study(self):
        print("Учусь на отлично!")

class Bad(Student):
    def study(self):
        print("Опять двойка...")

class Average(Student):
    def study(self):
        print("Ну, нормально вроде...")

class Journal:
    def __init__(self):
        self.students = []

    def add_students(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student.name)

    def students_study(self):
        for student in self.students:
            student.study()

spisok = Journal()

instance_one = Bad('alesha', 10)
instance_two = Average('vitya', 10)
instance_three = ExcellentStudent('sasha', 10)

spisok.add_students(instance_one)
spisok.add_students(instance_two)
spisok.add_students(instance_three)

spisok.show_students()
spisok.students_study()

# 🧱 Структура:
# Класс Task:
# Поля:
# title — название задачи
# description — описание
# completed — выполнена ли задача (bool, по умолчанию False)
# Методы:
# mark_completed() — отмечает задачу выполненной
# __str__() — строковое представление задачи
# Класс TaskManager:
# Хранит список задач
# Методы:
# add_task(task) — добавляет задачу (проверка через isinstance)
# show_tasks() — показывает все задачи с их статусом
# show_incomplete_tasks() — только невыполненные
# complete_task(title) — ищет по названию и отмечает как выполненную

