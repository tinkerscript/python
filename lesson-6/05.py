class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} рисует линию')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} проводит черту')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} подчёркивает')


pen = Pen('Паркер')
pen.draw()

pencil = Pencil('Кох-и-нур')
pencil.draw()

handle = Handle('Копик')
handle.draw()
