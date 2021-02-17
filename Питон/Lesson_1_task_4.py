number_user = int(input('Введите целое число'))
i = 0
while True:
    a = number_user % 10
    number_user = number_user // 10
    if i <= a:
        i = a
    if number_user < 10:
        if i <= number_user:
            i = number_user
        else:
            break

print(i)