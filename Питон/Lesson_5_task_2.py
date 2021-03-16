count_line = 0
with open('test_task_2.txt') as file:
    for line in file:
        count_line += 1
        string = len(line.split(' '))
        print(f'Строка {count_line}: кол-во слов - {string} ')
    print(f'количество строк {count_line}')