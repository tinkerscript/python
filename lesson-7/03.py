class Cell:
    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        return self.cells_count + other.cells_count

    def __sub__(self, other):
        result = self.cells_count - other.cells_count

        if result <= 0:
            raise ArithmeticError('Результат вычитания не может быть меньше нуля')

        return result

    def __mul__(self, other):
        return self.cells_count * other.cells_count

    def __truediv__(self, other):
        return self.cells_count / other.cells_count

    def make_order(self, n):
        rows_count = self.cells_count // n
        rest_count = self.cells_count % n

        result = '\n'.join('*'.join('' for d in range(n + 1)) for d in range(rows_count))

        if rest_count > 0:
            result += '\n' + '*'.join('' for d in range(rest_count + 1))

        return result


cell1 = Cell(3)
cell2 = Cell(5)

print(cell1 + cell2)
# 8

try:
    print(cell1 - cell2)
except ArithmeticError as e:
    print(e)
    # Результат вычитания не может быть меньше нуля

print(cell2 - cell1)
# 2

print(cell1 * cell2)
# 15

print(cell1 / cell2)
# 0.6

cell3 = Cell(12)
print(cell3.make_order(5))

'''
*****
*****
**
'''
