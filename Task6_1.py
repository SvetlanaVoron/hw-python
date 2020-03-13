# Задание 1 +. Не совсем поняла первое задание, что именно нужно использовать для автоматичесокго переключения цветов
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.color = color

    def running(self):
        print((self.color))
        if self.color == "зеленый":
            print((self.color))
            sleep(5)
        if self.color == "желтый":
            sleep(2)
        if self.color == "красный":
            sleep(5)
tl_1 = TrafficLight("Зеленый")
tl_1.running()
tl_1 = TrafficLight("Желтый")
tl_1.running()
tl_1 = TrafficLight("Красный")
tl_1.running()

