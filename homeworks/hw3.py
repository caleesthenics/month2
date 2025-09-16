class Person:

    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        print(f'Меня зовут {self.name}, я родился {self.__birth_date}, и я {self.__occupation}')

    @property
    def occupation_getter(self):
        return self.__occupation

    @property
    def higher_education_getter(self):
        return self.__higher_education

    @property
    def birth_date_getter(self):
        return self.__birth_date

class Classmate(Person):

    def __init__(self,name , birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        print(f'Всем привет меня зовут {self.name},я твой одноклассник ,'
              f'  родился {self.birth_date_getter}, и я {self.occupation_getter},'
              f' мы вместе учимся в {self.group} классе,'
              f'высшее образование {self.higher_education_getter}')

class Friend(Person):

    def __init__(self,name , birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Всем привет меня зовут {self.name},я твой друг ,'
              f'  родился {self.birth_date_getter}, и я {self.occupation_getter},'
              f'моё увлечение {self.hobby},'
              f'высшее образование {self.higher_education_getter}')

cm = Classmate('Anvar', '18.12.02', 'temshik', 'True', '11 B')
cm1 = Classmate('Artur', '19.10.02', 'temshik', 'True', '11 B')
fr = Friend('Danil', '14.06.97', 'bezrabotnii', 'False', 'Football' )

for human in [cm, cm1, fr]:
    human.introduce()