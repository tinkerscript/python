from random import randint


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = []

    def set(self, data):
        self.data = data

    def set_random(self):
        self.data = []

        for i in range(self.width):
            row = []

            for j in range(self.height):
                row.append(randint(0, 9))

            self.data.append(row)

    def __str__(self):
        return '\n'.join(' '.join(str(x) for x in y) for y in self.data)

    def __add__(self, other):
        rows = []

        for i in range(len(self.data)):
            row = []

            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])

            rows.append(row)

        result = Matrix(self.width, self.height)
        result.set(rows)
        return result


m1 = Matrix(2, 2)
m1.set_random()
m2 = Matrix(2, 2)
m2.set_random()

print('Матрица №1:')
print(m1)

print('Матрица №2:')
print(m2)

m3 = m1 + m2
print('Результат сложения матриц:')
print(m3)
