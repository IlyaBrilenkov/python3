import random

n = int(input('Введите количество чисел:'))
number = []

for i in range(n):
    number.append(random.randrange(1,10))

print(number)

num = number[0]
max_occ = 0
for i in range(n):
    occ = 0
    for k in range(i, n):
        if number[i] == number[k]:
            occ += 1
    if occ > max_occ:
        max_frq = occ
        num = number[i]

if max_occ > 1:
    print(max_occ, 'раз(а) встречается число', num)
else:
    print('Вcе числа уникальны')