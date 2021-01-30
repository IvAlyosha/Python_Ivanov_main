name = input('Введите свое имя ')
surname = input('Введите фамилию ')
age = int(input('Укажите свой возраст '))
weight = int(input('Укажите свой вес '))
if (age <= 30) and (weight >= 50 and weight <= 120):
    print(name, ', вы в хорошем состоянии')
elif (age > 30 and age < 40) and (weight <= 50 and weight >= 120):
    print(name, ', вам нужно заняться собой')
elif (age >= 40) and (weight <= 50 and weight >= 120):
    print(name, ', вам требуется врачебный осмотр')
else:
    print('Вам нужен осмотр')