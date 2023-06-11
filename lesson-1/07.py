a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

result = a
days = 1

while result < b:
    result += result / 10
    days += 1

print(days)
