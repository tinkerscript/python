revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

profitability = revenue - costs

if profitability > 0:
    print('Фирма приносит прибыль')
    print(f'Рентабельность составляет {round(profitability / revenue, 2) * 100}%')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль в расчёте на одного сотрудника составляет {revenue / employees}')
elif profitability < 0:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
