class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'{self.name} имеет скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        message = f'{self.name} имеет скорость {self.speed}'

        if self.speed > 60:
            message = f'{message}. Скорость превышена!'

        print(message)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        message = f'{self.name} имеет скорость {self.speed}'

        if self.speed > 40:
            message = f'{message}. Скорость превышена!'

        print(message)


class PoliceCar(Car):
    is_police = True


lada = TownCar(50, 'red', 'Лада Гранта')
zil = WorkCar(45, 'green', 'ЗИЛ')

lada.go()
lada.turn('направо')
lada.show_speed()

zil.go()
zil.turn('налево')
zil.show_speed()
zil.stop()
