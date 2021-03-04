def upper_str(str_user):
    """Приведение строки к верхнему регистру"""
    parsing_str = parsing_str_user(str_user)
    result_str = ''
    for item in parsing_str:
        first_letter = item[0]
        result_str = result_str + ' ' + first_letter.upper() + item[1:]
    return print(result_str)


def parsing_str_user(str_user):
    """Функция разбивает строку"""
    str_result = str_user.split()
    return str_result


upper_str(input('введите текст'))
