def search(quantity, numeral, desired_number, n):

    nomber = input('Введите число:')
    desired_number = desired_number + nomber.count(numeral)
    n += 1
    if n == quantity:
        return print(f'Количество вхождений: {desired_number}')
    else:
        return (search(quantity, numeral, desired_number, n))


quantity = int(input('Введите количество чисел:'))
numeral = input('Введите искомое число:')
desired_number = 0
n = 0

search(quantity, numeral, desired_number, n)

# n - счетчик