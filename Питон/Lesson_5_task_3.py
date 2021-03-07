with open('test_task_3.txt', "r", encoding='utf-8') as file:
    for line in file:
        string = line.split(' ')
        if int(string[1]) >= 20000:
            print(string[0])
