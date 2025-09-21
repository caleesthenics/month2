#:QW - завершить merge при конфликте
from lessons.lesson1 import Car

class Money:
    def __init__(self, amount = 0):
        self.amount = amount

#mul - multiple, eq - equal, gt - greater than -self > other, ge - greather than or equal ,
    # lt - less than, le less than or equal) - "Dunder Methods - magic methods double underscore"

    def __str__(self):
        return f"money : {self.amount}"

    # def sum(self):
    #     return (self.amount * 2)

    def __add__(self, other):
        return Money(self.amount + other.amount) #атрибутам можно придумывать другую логику, самому методу - нет

    def __sub__(self, other):
        return Money(self.amount - other.amount) # tut to je samoe

adilet = Money(250)

cash = Money(100)



print(total)