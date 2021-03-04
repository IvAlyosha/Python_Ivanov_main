import random

list = [random.randint(1,1000) for i in range(0,random.randint(10,50))]
print(list)
result_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(result_list)