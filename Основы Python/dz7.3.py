import copy
import random
def transform_list(list):
    new_list=copy.copy(list)
    new_list=[number**2 if number>0 else number for number in new_list]
    return new_list

list=[random.randint(-100,100) for i in range (0,20)]
print(list)
print(transform_list(list))
