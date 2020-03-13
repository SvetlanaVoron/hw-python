# Задание 2 +
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def road_weight(self):
        weight_r = self._length * self._width * (25 / 100) * 5
        print(f"Расчет массы дороги: {self._length} м * {self._width} м * 25 кг * 5 см = {int(weight_r)} т")

road_1 = Road(5000, 20)
road_1.road_weight()



