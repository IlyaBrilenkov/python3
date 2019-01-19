import random

n = int(input('Введите количество чисел:'))
number = []

for i in range(n):
    number.append(random.randrange(-10,10))

print(number)

number_2 = []
for i in number:
    if i < 0:
        number_2.append(i)

print(max(number_2))
