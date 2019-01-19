def calculator(number_1, number_2):
    while True:
        print('%.2f' % (number_1))
        sign = input("Выберите действие: '+', '-', '/', '*'. Для завершения введите '0' ")

        if number_1 == 0 and sign == '/':
            print('Делить на ноль нельзя! Выберите другое действие')
            continue

        if sign == '0':
            return print('До свидания')

        if sign == '+' or sign == '-' or sign == '/' or sign == '*':
            break

        print('Введите корректный символ!')

    number_2 = float(input('Введите второе число:'))

    if sign == '+':
        number_1 = number_1 + number_2
    if sign == '-':
        number_1 = number_1 - number_2
    if sign == '/':
        number_1 = number_1 / number_2
    if sign == '*':
        number_1 = number_1 * number_2

    return calculator(number_1, number_2)


number_1 = float(input('Введите первое число:'))

calculator(number_1, '')
