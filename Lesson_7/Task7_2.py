# Задание 2

from abc import ABC, abstractmethod

class clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def textile(self):
        pass

    @property
    def total(self):
        total = self.total_coat + self.total_suit
        return total


class coat(clothes):
    @property
    def textile(self):
        total_coat = round((self.param / 6.5) + 0.5)
        return total_coat

class suit(clothes):
    @property
    def textile(self):
        total_suit = round((2 * self.param) + 0.3)
        return total_suit


coat = coat(54)
suit = suit(190)
print(coat.textile)
print(suit.textile)
print(clothes.total)


