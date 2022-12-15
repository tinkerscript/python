lines_count = 0
words_count = 0

with open('02.txt') as f:
    for line in f:
        lines_count += 1
        words_count += len(line.split(' '))

print(f'Количество строк в файле 02.txt: {lines_count}')
print(f'Количество слов в файле 02.txt: {words_count}')

'''
02.txt:
Однажды, в студёную зимнюю пору,
Я из лесу вышел. Был сильный мороз.
Гляжу, поднимается медленно в гору
Лошадка, везущая хворосту воз.

Вывод:
Количество строк в файле 02.txt: 4
Количество слов в файле 02.txt: 21
'''
