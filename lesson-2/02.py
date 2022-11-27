count = int(input('Введите количество элементов в списке: '))
my_list = []

for index in range(count):
    my_list.append(input(f'Введите элемент №{index}: '))

index = 0

while index < len(my_list) - 1:
    item = my_list[index]
    my_list[index] = my_list[index + 1]
    my_list[index + 1] = item
    index += 2

print(my_list)
