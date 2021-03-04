def division (one_number, two_number):
    """Функиция деления двух чисел"""
    try:
        return print(one_number/two_number)
    except ZeroDivisionError:
            print('на ноль делить нельзя')

division(int(input('введите число 1')), int(input('введите число 2')))