answer = input('Введите натуральное число:')

even = 0
odd = 0

for i in answer:
    if int(i) % 2 != 0:
        odd += 1
    else:
        even += 1

print(f'четных цифр: {even}, нечетных: {odd}')