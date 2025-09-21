from distance import Distance

hundred = Distance(100, "cm")
two_hundred = Distance(200, "m")

summa = hundred + two_hundred
print(summa)

ravno = two_hundred == hundred
print(ravno)

raznica = two_hundred - hundred
print(raznica)

print(hundred)