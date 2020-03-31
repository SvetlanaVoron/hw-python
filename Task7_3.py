# Задание 3

class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def make_order(self, length):
        lines = self.numbers // length
        i = 0
        while i < lines:
            i += 1
            print( "*" * length)
        print ("*" * (self.numbers % length))


    def __str__(self):
        return self.numbers

    def __add__(self, other):
        print(f"Сумма ячеек: {self.numbers + other.numbers}")

    def __sub__(self, other):
        result = self.numbers - other.numbers
        if result > 0:
            print(f"Разница ячеек: {result}")
        else:
            print("Вычитание невозможно, т.к. в первой клетке меньше ячеек чем во второнй или кол-во равно")

    def __mul__(self, other):
        print(f"Произведение ячеек: {self.numbers * other.numbers}")

    def __truediv__(self, other):
        print(f"Отношение ячеек: {self.numbers / other.numbers:.2f}")

c_obj_1 = Cell(50)
c_obj_2 = Cell(40)
c_obj_1 + c_obj_2
c_obj_1 - c_obj_2
c_obj_1 * c_obj_2
c_obj_1 / c_obj_2

c_obj_1.make_order(19)
print("---")
c_obj_2.make_order(7)


