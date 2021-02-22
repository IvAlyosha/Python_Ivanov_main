list_user = input('введите слова через пробелы')
list_result = list_user.split()
i = 0
for index in list_result:
    print(f'{i})', list_result[i][0:10])
    i += 1