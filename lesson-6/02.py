class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate(self, spec_mass, depth):
        return self._width * self._length * spec_mass * depth


road = Road(20, 5000)
print(f'Масса асфальта составит {road.calculate(25, 5) / 1000} тонн')
