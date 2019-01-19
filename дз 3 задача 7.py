import random

n = int(input('Введите количество чисел:'))
number = []

for i in range(n):
    number.append(random.randrange(1,10))

print(number)

mi = min(number)
a = 0

while a < 2:
    if a == 2:
        break
    for c, i in enumerate(number):
        if i == mi:
            print(i)
            number.pop(c)
            a += 1
            mi = min(number)
            break
