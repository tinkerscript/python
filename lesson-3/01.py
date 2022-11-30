def my_function(a, b):
    return a / b


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

try:
    print(my_function(first, second))
except ZeroDivisionError:
    print('Деление на ноль запрещено')
