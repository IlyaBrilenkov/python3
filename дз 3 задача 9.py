column = 4
line = 4
matrix = []

for i in range(column):
    a = []
    for i in range(line):
        a.append(int(input('Введите число: ')))
    print(a)
    print()
    matrix.append(a)

for i in matrix:
    print(i)

numbers = []
for i in range(4):
    mi = sum(a)
    for j in range(4):
        if matrix[j][i] < mi:
            mi = matrix[j][i]
    numbers.append(mi)

print(f'максимальный элемент среди минимальных элементов столбцов: {max(numbers)}')