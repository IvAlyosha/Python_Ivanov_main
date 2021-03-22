from functools import reduce
result = {}
with open('test_task_6.txt', encoding='utf-8') as file_read:
    for line in file_read:
        list_number = line.replace(":", ".").replace(",", ".").replace(" ", ".").replace("(л)", ".").replace("(пр)", ".").replace("(лаб)",".").replace("—",".").replace("\n",".").split('.')
        name_subject = list_number[0]
        list_number = [int(item) for item in list_number if item.isdigit()]
        result[name_subject] = reduce(lambda x, y: x + y, list_number)
print(result)