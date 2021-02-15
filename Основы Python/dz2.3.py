import random
list_1=[i for i in range(0, random.randint(1,27))]
result=[]
for number in list_1:
    if list_1.count(number) == 1:
        result.append(number)
print(result)