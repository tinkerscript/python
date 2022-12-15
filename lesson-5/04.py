numerals = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}


def replace_numerals(s):
    for key, value in numerals.items():
        s = s.replace(key, value)

    return s


lines = []

with open('04_in.txt') as f:
    for line in f:
        lines.append(replace_numerals(line))

with open('04_out.txt', 'w') as f:
    f.writelines(lines)
