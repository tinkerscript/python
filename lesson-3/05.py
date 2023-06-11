def aggregate(s):
    items = s.split(' ')

    result = 0
    q = False

    for item in items:
        if item == 'q':
            q = True
            break
        else:
            result += int(item)

    return result, q


print('Введите числа, разделенные пробелами или q для выхода: ')

end = False

while not end:
    string = input()
    numbers_sum, need_to_quit = aggregate(string)
    end = need_to_quit

    print(numbers_sum)
