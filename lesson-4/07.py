from math import factorial


def fact(target):
    for num in range(factorial(target)):
        yield num + 1


n = int(input('Введите n: '))
c = 0

for el in fact(n):
    if c >= n:
        break

    print(el)
    c += 1
