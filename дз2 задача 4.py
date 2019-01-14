n = int(input('Введите количество повторений n:'))
element = 1
sum = 0
for i in range(n):
    sum += element
    element /= -2
print(sum)