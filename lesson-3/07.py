def int_func(word):
    return word.capitalize()


string = input('Введите слова, разделенные пробелами: ')

words = string.split(' ')
capitalized_words = []

for item in words:
    capitalized_words.append(int_func(item))

print(''.join(capitalized_words))
