class Distance:
    def __init__(self, value , unit):
        self.value = value
        self.unit = unit
        self.average_unit = 'm'

    def __str__(self):
        return F'Дистанция = {self.convert()}{self.average_unit}'

    def __add__(self, other):
        return Distance((self.convert() + other.convert()), self.average_unit)

    def __sub__(self, other):
        result = self.convert() - other.convert()
        if result < 0:
            return 'ne mogu vi4est iz menshego bolshee(('
        return Distance(result, self.average_unit)


    def __eq__(self, other):
        return self.convert() == other.convert()

    def convert(self):
        if self.unit == "m":
            return self.value
        elif  self.unit == "km":
            return self.value * 1000
        elif self.unit == "cm":
            return self.value * 0.01
