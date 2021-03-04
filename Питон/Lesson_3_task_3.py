def max_number(*numbers):
    """Функция выводит сумму максимальных двух чисел"""
    numbers = list(numbers)
    max_number_1 = max(numbers)
    numbers.remove(max_number_1)
    max_number_2 = max(numbers)
    return print(max_number_1+max_number_2)

max_number(int(input('Введите число')), int(input('Введите число')), int(input('Введите число')))
