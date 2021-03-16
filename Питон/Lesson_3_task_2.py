def data_user(name_user, second_name, *arg):
    """Функция выводит информацию от пользователя в одну строчку"""
    list = ''
    for name in arg:
        list = f'{list}  {name}'
    return print(f'Данные по пользователю {name_user} {second_name}: {list}')

data_user(input('введите имя'), input('введите фамилию'), input('Введите год рождения'), input('Введите город проживания'), input('введите email'), input('введите номер телефона'))