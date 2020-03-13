# Задание 4 +
class Car:
    def __init__(self, speed, color, name, is_police, direction=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print(f'Car "{self.name}" color {self.color} goes')

    def stop(self):
        print(f'Car "{self.name}" color {self.color} stops')

    def turn(self):
        if self.direction is not None:
            print(f'Car "{self.name}" color {self.color} turns to {self.direction}')
        else:
            print(f'Car "{self.name}" color {self.color} turns')


    def show_speed(self):
        print(f'Current speed is: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Speed is over aloweded ')
        else:
            print('Speed is aloweded ')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Speed is over aloweded ')
        else:
            print('Speed is aloweded ')


class PoliceCar(Car):
    pass


toyota = TownCar(100, "Черная", "Toyota", False)
toyota.show_speed()
porshe = SportCar(200, "Красная", "Porshe", False, "right")
porshe.turn()
bmw = WorkCar(30, "Синяя", "BMW", False)
bmw.show_speed()
lada = PoliceCar(80, "Белая", "Лада", True)
lada.stop()