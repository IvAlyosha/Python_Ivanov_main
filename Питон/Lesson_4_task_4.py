list_start = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(list_start)
result_list = [list_start for i in list_start if list_start.count(i) == 1]
print(result_list)