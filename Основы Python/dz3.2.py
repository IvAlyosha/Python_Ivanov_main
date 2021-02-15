import random
start_range = 0
end_range = 100
number = random.randint(start_range, end_range)
is_winner = False
while not is_winner:
    answer_user = int(input(f'Это число = {number}. Нажмите вариант ответа 1)= 2)> 3)<'))
    if answer_user == 1:
        is_winner = True
    elif answer_user ==2:
        start_range = number
        number = random.randint(start_range,end_range)
    elif answer_user ==3:
        end_range = number
        number=random.randint(start_range,end_range)
else:
    print('Победа')