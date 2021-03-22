dict = {
    'One':'один',
    'Two':'два',
    'Three':'три',
    'Four': 'четыре'
}
with open('test_task_4_write.txt','w', encoding='utf-8') as file_write:
    with open('test_task_4.txt', "r", encoding='utf-8') as file:
        for line in file:
            string = line.split(' — ')
            file_write.write(dict[string[0]] + ' — ' + string[1] + '\n')
