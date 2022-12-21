from abc import ABC, abstractmethod


class Inventory:
    def __init__(self):
        self._items = {}

    def take(self, item):
        item_type = item.get_item_type()

        if item_type not in self._items:
            self._items[item_type] = []

        self._items[item_type].append(item)

    def __str__(self):
        result = ''

        for item_type, items in self._items.items():
            result += f'{item_type}: {", ".join([str(item) for item in items])}\n'

        return result


class Storage(Inventory):
    def __send(self, unit, item_type):
        if item_type not in self._items:
            print('Данный тип техники не зарегистрирован')
            return

        if len(self._items[item_type]) == 0:
            print('Нет свободной техники данного типа')
            return

        item = self._items[item_type].pop()
        unit.take(item)

    def send(self, unit, item_type, count=None):
        if count is None:
            count = 1

        try:
            count = int(count)
        except TypeError:
            print('Количество должно быть числом')
            return

        for i in range(0, count or 1):
            self.__send(unit, item_type)


class Unit(Inventory):
    instances = []

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.__class__.instances.append(self)

    def __str__(self):
        return f'{self.name}:\n{super().__str__()}'

    @classmethod
    def report_all(cls):
        for unit in cls.instances:
            print(unit)


class Product(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def get_item_type(self):
        pass


class Printer(Product):
    def get_item_type(self):
        return 'printer'


class Copier(Product):
    def get_item_type(self):
        return 'copier'


class Scanner(Product):
    def get_item_type(self):
        return 'scanner'


storage = Storage()

storage.take(Printer('HP Laser 107r'))
storage.take(Printer('Brother HL1223WR'))
storage.take(Printer('Canon G1420'))
storage.take(Printer('Epson L805'))

storage.take(Copier('Xerox Fluid'))

storage.take(Scanner('Canon CanoScan LiDE400'))
storage.take(Scanner('HP ScanJet Pro 2000'))

head_office = Unit('Главный офис')
branch_office = Unit('Калужский филиал')

storage.send(head_office, 'printer', 2)
storage.send(head_office, 'copier')
storage.send(head_office, 'scanner')

storage.send(branch_office, 'printer')
storage.send(branch_office, 'copier')  # Выведет: "Нет свободной техники данного типа"
storage.send(branch_office, 'scanner')

Unit.report_all()
'''
Главный офис:
printer: Epson L805, Canon G1420
copier: Xerox Fluid
scanner: HP ScanJet Pro 2000

Калужский филиал:
printer: Brother HL1223WR
scanner: Canon CanoScan LiDE400
'''
