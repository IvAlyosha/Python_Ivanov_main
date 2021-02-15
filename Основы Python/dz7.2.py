import random

list_number=[random.randint(-100,100) for i in range (0,20)]
print(list_number)
list_sort=[number for number in list_number if number%3==0 and number>0 and number%4!=0]
print(list_sort)