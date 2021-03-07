from sys import argv

script_name, rate_hour, hour, bonus = argv

print('Зарплата сотрудника составляет =', int(rate_hour)*int(hour) + int(bonus))
