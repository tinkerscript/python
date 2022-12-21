class CustomException(Exception):
    def __init__(self, message):
        self.message = message


def try_to_append(array, s):
    if not s.isnumeric():
        raise CustomException(f'{s} не является числом')

    array.append(float(s))


numbers = []

while True:
    data = input('Введите число (stop - выход): ')

    if data == 'stop':
        break

    try:
        try_to_append(numbers, data)
    except CustomException as e:
        print(e.message)

print(numbers)
