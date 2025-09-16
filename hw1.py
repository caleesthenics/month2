class Person:
    def __init__(self, name, birt_date, occupation, higher_education):
        self.name = name
        self.birt_date = birt_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f'Меня зовут {self.name}, я родился {self.birt_date}, и я {self.occupation}')

michael_jordan = Person('Michael', '17.02.1963', 'Basketball Player', 'True')
michael_jordan.introduce()

kobe_bryant = Person('Kobe', '23.08.1978', 'basketball player', 'true')
kobe_bryant.introduce()

steph_curry = Person('Steph', '14.03.1988', 'basketball player', 'true')
steph_curry.introduce()