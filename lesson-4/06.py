from itertools import count, cycle


def script_1(number):
    for el in count(number):
        print(el)

        if el > number + 7:
            break


def script_2():
    x = 0

    for el in cycle(['test', 42, True]):
        print(el)
        x += 1

        if x > 7:
            break


script_1(0)
script_2()
