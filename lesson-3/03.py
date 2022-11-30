def compare(a, b, c):
    list_to_sort = [a, b, c]
    list_to_sort.sort(reverse=True)
    return list_to_sort[0] + list_to_sort[1]


print(compare(7, 1, 5))
