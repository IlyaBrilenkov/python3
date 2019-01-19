import random

n = 0
number = int(random.random() * 100)

while True:
    answer = int(input('Угадай число:'))

    if number == answer:
        print('Поздравляю, число угадано!')
        break
    elif number > answer:
        print('Загаданное число больше')
    elif number < answer:
        print('Загаданное число меньше')

    n += 1
    if n == 10:
        print(f'Неудача! загаданное число - {number}')
