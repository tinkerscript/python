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


cell1 = Cell(3)
cell2 = Cell(5)

print(cell1 + cell2)

try:
    print(cell1 - cell2)
except ArithmeticError as e:
    print(e)

print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
