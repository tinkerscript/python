month_number = int(input('Введите номер месяца: '))

if month_number < 1 or month_number > 12:
    print('Введите число от 1 до 12')
    quit()

seasons_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

print(seasons_list[month_number - 1])
