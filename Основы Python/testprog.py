print('Медицинская анкета \n ')
name = input('Введите имя пациента: ')
age = int(input('Введите возраст пациента: '))
weight = int(input('Введите вес пациента: '))

if age <= 30:
    if 50 <= weight <= 120:
        print(name, ', Возраст - ', age, ', вес - ', weight, '. Пациент в хорошем состоянии и молод!')
    else:
        print(name, ', Возраст - ', age, ', вес - ', weight, '. Пациент еще молод и может всё исправить!')
if age > 30:
    if age > 40 and (weight < 50 or weight > 120):
        print(name, ', Возраст - ', age, ', вес - ', weight, '. Пациенту нужен врачебный осмотр!!!')
    elif 50 <= weight <= 120:
        print(name, ', Возраст - ', age, ', вес - ', weight, '. Пациент уже не молодой, но в норме.')
    else:
        print(name, ', Возраст - ', age, ', вес - ', weight, '. Пациенту следует заняться собой...')