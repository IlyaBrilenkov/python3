n = int(input('Введите число n:'))
sum_1 = 0

for i in range(n + 1):
    sum_1 = sum_1 + i

sum_2 = n * (n + 1) / 2

print(f'{sum_1} = {sum_2}')
