import random
list_1=[i for i in range(0, random.randint(1,27))]
print(list_1)
list_2=[i for i in range(0, random.randint(1,27))]
print(list_2)
for number in list_1[:]:
    if number in list_2:
        list_1.remove(number)
print(list_1)
result=list(set(list_1) ^ set(list_2))
print(list_1)

