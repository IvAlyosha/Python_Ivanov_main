from itertools import count,cycle
import random


def iterate_integer (start, end):
    """Функция итерации целых чисел по заданным значениям"""
    for i in count(start):
        if i >=end:
            break
        else:
            print(i)
iterate_integer(10,40)

def iterate_list (list):
    """функция итерации передаваемого списка"""
    count = 0
    for i in cycle(list):
        if count >= len(list):
            break
        else:
            count += 1
            print(i)

list = [random.randint(1,1000) for i in range(0,random.randint(10,50))]
iterate_list(list)


