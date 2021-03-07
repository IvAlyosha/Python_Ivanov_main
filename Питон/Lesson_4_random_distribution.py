import random

re_dict = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0
}
for item in range(10000000):
    re_dict[random.randint(1,10)] += 1

print(re_dict)