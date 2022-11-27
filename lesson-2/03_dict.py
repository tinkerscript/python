month_number = int(input('Введите номер месяца: '))

if month_number < 1 or month_number > 12:
    print('Введите число от 1 до 12')
    quit()

seasons_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима'
}

print(seasons_dict[month_number])
