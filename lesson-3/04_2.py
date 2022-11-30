def my_func(x, y):
    if y == 0:
        return 1

    result = x

    for i in range(1, y):
        result *= x

    return result


print(my_func(2, 3))
