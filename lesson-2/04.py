string = input('Введите строку: ')
words = string.split(' ')

for index in range(len(words)):
    print(f'{index + 1}. {words[index].capitalize()}')

"""
Введите строку: тест привет пока
1. Тест
2. Привет
3. Пока
"""