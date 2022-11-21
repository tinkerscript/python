number = int(input('Введите целое положительное число: '))

maximum = 0

while number > 0:
    digit = number % 10

    if digit > maximum:
        maximum = digit

    number //= 10

print(maximum)
