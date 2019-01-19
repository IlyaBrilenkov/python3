number = []
two = []

while True:
    answer = input('введите число в массив, для выхода введите "q":')
    if answer == 'q':
        break
    number.append(answer)

for c, i in enumerate(number):
    if int(i) % 2 == 0:
        two.append(c)

print(f'индексы четных чисел массива: {two}')