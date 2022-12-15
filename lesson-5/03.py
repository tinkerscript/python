total_count = 0
total_sum = 0

print('Список сотрудников с окладом менее 20000.00:')

with open('03.txt') as f:
    for line in f:
        total_count += 1
        name, salary_string = line.split(' ')
        salary = float(salary_string)

        if salary < 20000.00:
            print(name)

        total_sum += salary

print(f'Средний оклад составляет {total_sum / total_count}')
