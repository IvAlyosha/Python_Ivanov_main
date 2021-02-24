number_list = int(input('Введите количество элементов списка'))
user_list = [input(f'Введите {list} элемент списка') for list in range(0, number_list)]
print(user_list)
i = 0
while i < number_list-1:
    i += 1
    if i == number_list-1 and number_list % 2 != 0:
        break
    user_list[i], user_list[i-1] = user_list[i-1], user_list[i]
print(user_list)