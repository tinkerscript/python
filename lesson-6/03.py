class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


manager = Position('Иван', 'Петров', 'менеджер', 15000, 3000)
print(f'Сотрудник {manager.get_full_name()} имеет доход {manager.get_total_income()}')
