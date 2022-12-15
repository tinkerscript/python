f = open('data.txt', 'w')
print('Введите данные построчно')
print('Пустая строка - запись в файл и конец программы')

while True:
    line = input('Введите строку: ')

    if line == '':
        break

    f.write(line + '\n')

f.close()
