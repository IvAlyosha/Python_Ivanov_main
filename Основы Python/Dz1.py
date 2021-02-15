name = input('Введите свое имя ')
surname = input('Введите фамилию ')
age = int(input('Укажите свой возраст '))
weight = int(input('Укажите свой вес '))
if (age <= 30) and (weight >= 50 and weight <= 120):
    print(name, ', вы в хорошем состоянии')
elif (age > 30 and age < 40) and (weight <= 50 and weight >= 120):
    print(name, surname, age, 'год, вес', weight, ' - Нужно поработать над собой')
elif (age >= 40) and (weight <= 50 and weight >= 120):
    print(name, surname, age, 'год, вес', weight, ' - Следует обратится к врачу')
else:
    print('Вам ничего не поможет')
