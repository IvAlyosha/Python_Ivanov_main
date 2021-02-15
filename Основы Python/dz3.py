import random
number = random.randint(0, 100)
answer_user = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
set_levels = int(input('Выберете один из уровней сложности'))
max_count = levels[set_levels]
user_count = int(input('Введите количество пользователей'))
users = []
is_winner = False
winner_name = ''
for i in range(user_count):
    user_name = input('Введите имя пользователя')
    users.append(user_name)
while not is_winner:
    if count >= max_count:
        print('Все пользователи проиграли')
        break
    count += 1
    print('Попытка №', count)
    for user in users:
        print(f'Ход пользователя: {user}')
        answer_user = int(input('Введите число от 1 до 100'))
        if answer_user == number:
            is_winner = True
            winner_name = user
            break
        elif answer_user < number:
            print('Слишком маленькое число')
        elif answer_user > number:
            print('Слишком большое число')

else:
    print(f'Победа {winner_name}')