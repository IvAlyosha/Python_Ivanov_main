def exponentiation(x, y):
    """Функция возведения в степень"""
    #return print(x**(-y))
    sum = 1
    for i in range(0,y):
        sum = sum*1/x
    return print(sum)
exponentiation(int(input('Введите число')),int(input('Укажите степень')))