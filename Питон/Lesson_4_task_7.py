import math
def fact(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    elif x < 0:
        print('Введите число больше 0')
    elif x > 0:
        while b < x:
            a = a * b
            b += 1
            print(a)
            yield a
n = int(input('Введите число'))
for el in fact(n):
    print(el)