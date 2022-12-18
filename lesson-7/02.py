from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def calculate_expenses(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def calculate_expenses(self):
        return self.size * 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, name, growth):
        super().__init__(name)
        self.growth = growth

    @property
    def calculate_expenses(self):
        return self.growth * 2 + 0.3


coat = Coat('Кашемировое пальто', 50)
print(coat.calculate_expenses)

suite = Suite('Твидовый костюм', 180)
print(suite.calculate_expenses)
