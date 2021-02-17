revenue = int(input('Введите выручку вашей фирмы'))
costs = int(input('Введите издержки вашей фирмы'))
profit = revenue - costs
profitability = profit / revenue
lession = costs - revenue
if revenue > costs:
    print('Ваша фирма получает прибыль = ', profit)
    print('Рентабельность вашей фирмы = ', profitability)
    quantity_employees = int(input('Введите количество сотрудников'))
    profit_per_employess = quantity_employees / profit
    print('Прибыль на одного сотрудника = ', profit_per_employess)
elif revenue < costs:
    print('Убыток вашей фирмы состовляет = ', lession)
else:
    print('Ваша фирма не получает прибыли и не работает в убыток')