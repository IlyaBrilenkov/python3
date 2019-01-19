import random

n = int(input('Введите количество чисел:'))
number = []

for i in range(n):
    number.append(random.randrange(1,10))

print(number)

ma = max(number)
mi = min(number)

for c, i in enumerate(number):
    if i == ma:
        number.pop(c)
    elif i == mi:
        number.pop(c)

print(sum(number))
