def sum_str_numb():
    """Функция считает сумму чисел через пробел до указания !"""
    number = input_and_parsing_str()
    sum_number = 0
    while True:
        for item in number:
            if item == '!':
                return print(sum_number)
            sum_number = int(item) + sum_number
        number = input_and_parsing_str()


def input_and_parsing_str():
    """Функция запрашивает число у пользователя и разбивает строку"""
    user_input = input('Введите числа через проблел, если хотите закончить введите "!"')
    number = user_input.split()
    return number


if __name__ == '__main__':
    sum_str_numb()
