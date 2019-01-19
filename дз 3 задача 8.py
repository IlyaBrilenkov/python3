column = 4
line = 5
matrix = []

for i in range(column):
    a = []
    for i in range(line):
        if i < 4:
            a.append(int(input('Введите число: ')))
        else:
            a.append(sum(a))
    print(a)
    matrix.append(a)

for i in matrix:
    print(i)
