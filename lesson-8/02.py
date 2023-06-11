class CustomException(Exception):
    def __init__(self, message):
        self.message = message


def divide(a, b):
    if b == 0:
        raise CustomException('Division by zero')

    return a / b


number_a = int(input('Введите делимое: '))
number_b = int(input('Введите делитель: '))

try:
    result = divide(number_a, number_b)
    print(result)
except CustomException:
    print('На ноль делить нельзя')
