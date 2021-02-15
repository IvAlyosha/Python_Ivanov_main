import random

def random_number(number_list):
    number=None
    if number_list!=[]:
       number= random.choice(number_list)
    return number