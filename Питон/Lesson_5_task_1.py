with open('test_task_1.txt',"w") as file:
    user_data = input('Введите строку')
    while user_data != '':
        file.write(user_data + '\n')
        user_data = input('Введите строку')
