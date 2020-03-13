# Задание 5 +
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск письма  - {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск рисования  - {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск выделения - {self.title}')


pen_1 = Pen("Ручка")
pen_1.draw()
pencil_1 = Pencil("Карандаш")
pencil_1.draw()
handle_1 = Handle("Маркер")
handle_1.draw()
