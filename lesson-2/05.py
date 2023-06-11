my_list = [7, 5, 3, 3, 2]
new_item = int(input('Введите натуральное число: '))
index = 0

while index < len(my_list) and new_item <= my_list[index]:
    index += 1

my_list.insert(index, new_item)
print(my_list)
