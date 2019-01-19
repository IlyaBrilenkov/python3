numbers = []

for i in range(2,100):
    numbers.append(i)

for i in range(2,10):
    n = 0
    for b in numbers:
        if b % i == 0:
            n += 1
    print(f'числу {i} кратно {n} чисел из интервала 2-99')
