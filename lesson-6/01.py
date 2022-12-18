from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        while True:
            self.__set_next_color()

    def __set_next_color(self):
        print(f'Горит {self.__color} цвет')

        if self.__color == 'красный':
            sleep(7)
            next_color = 'жёлтый'
        elif self.__color == 'жёлтый':
            sleep(2)
            next_color = 'зелёный'
        else:
            sleep(5)
            next_color = 'красный'
            user_input = input('Выйти из программы? Y/n (по умолчанию Y)')

            if user_input == '' or user_input == 'Y':
                quit()

        self.__color = next_color


x = TrafficLight()
x.running()
