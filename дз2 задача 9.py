def counter(quantity, n, highest_number, sum_hn):
    sum = 0
    number = input('Введите число:')
    for i in number:
        sum += int(i)
    if sum > sum_hn:
        sum_hn = sum
        highest_number = number
    n += 1
    if n == quantity:
        return print(f'Наибольшее число по сумме цифр: {highest_number}, сумма его цифр: {sum_hn}')
    else:
        return (counter(quantity, n, highest_number, sum_hn))


quantity = int(input('Введите количество чисел:'))
n = 0
highest_number = 0
sum_hn = 0

counter(quantity, n, highest_number, sum_hn)
