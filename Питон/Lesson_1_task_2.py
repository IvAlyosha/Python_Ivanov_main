second_user = int(input('Введите количество секунд'))
hours = second_user // 60 // 60
minutes = int(((second_user / 60 / 60) - hours)*60)
second = int((((second_user / 60 / 60) - hours)*60 - minutes)*60)
print(hours, minutes, second)
