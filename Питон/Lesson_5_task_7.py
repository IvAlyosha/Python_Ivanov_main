from functools import reduce
import json
count_company = 0
profit_avarage_list = []
result_list_avarage = {}
result_list = []
with open('test_task_7.txt', encoding='utf-8') as file_read:
    for line in file_read:
        data_list = line.replace("\n", ' ').split(' ')
        profit_list = [int(item) for item in data_list if item.isdigit()]
        profit_list = reduce(lambda x, y: x - y, profit_list)
        result_list_avarage[data_list[0]] = profit_list
        if profit_list > 0:
            profit_avarage_list.append(profit_list)
            count_company += 1
    profit_avarage_list = {'profit_avarage': reduce(lambda x, y: x + y, profit_avarage_list)/count_company}
    result_list.append(result_list_avarage)
    result_list.append(profit_avarage_list)
    print(result_list)
with open("test_task_7.json", "w") as write_f:
    json.dump(result_list, write_f)



