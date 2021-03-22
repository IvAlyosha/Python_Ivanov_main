import random
from functools import reduce

list = [random.randint(1, 1000) for i in range(0, random.randint(10, 50))]
with open('test_task_5.txt', "w") as file:
    for i in list:
        i = str(i)
        file.write(i + ' ')


with open('test_task_5.txt') as file_read:
    for line in file_read:
        list_number = line.split(' ')
        list_number = [item for item in list_number if item != '']
    result = [int(item) for item in list_number]
    sum = reduce(lambda x, y: x+y, result)
print(sum)