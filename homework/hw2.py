class Person:

    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Меня зовут {self.name}, я родился {self.birth_date}, и я {self.occupation}')

class Classmate(Person):

    def __init__(self,name , birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        print(f'Всем привет меня зовут {self.name},я твой одноклассник ,  родился {self.birth_date}, и я {self.occupation}, мы вместе учимся в {self.group} классе')

class Friend(Person):

    def __init__(self,name , birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Всем привет меня зовут {self.name},я твой друг ,  родился {self.birth_date}, и я {self.occupation},моё увлечение {self.hobby}')

cm = Classmate('Anvar', '18.12.02', 'temshik', 'True', '11 B')
cm1 = Classmate('Artur', '19.10.02', 'temshik', 'True', '11 B')
fr = Friend('Danil', '14.06.97', 'bezrabotnii', 'False', 'Football' )

for human in [cm, cm1, fr]:
    human.introduce()