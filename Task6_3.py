# Задание 3 +

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._fix = _income["fix"]
        self._bonus = _income["bonus"]


class Position(Worker):
    def get_full_name(self):
        print(f"Фамилия: {self.surname}\nИмя: {self.name}\nДолжность: {self.position}")

    def get_total_income(self):
        i = self._fix + self._bonus
        print(f"Оклад: {self._fix}, бонус:{self._bonus}, суммарный доход:{i} \n")

p_1 = Position("Сергей", "Петров", "Менеджер", {"fix": 100, "bonus": 300})
p_1.get_full_name()
p_1.get_total_income()

# Задание 3 (v2 - но с ошибкой. попытка сделать строго как в задании)
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def income(self):
        self._income = self._income["fix"] + self._income["bonus"]
        return self.income

class Position(Worker):
    def get_full_name(self):
        print(f"Фамилия: {self.surname}\nИмя: {self.name}\nДолжность: {self.position}")

    def get_total_income(self):
        print(f"Cуммарный доход:{self.income(self)} \n")

p_1 = Position("Сергей", "Петров", "Менеджер", {"fix": 100, "bonus": 300})
p_1.get_full_name()
p_1.get_total_income()