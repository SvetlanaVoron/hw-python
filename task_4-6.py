#Задание 5
from itertools import count, cycle
#a
for el in count(int(input("Введите начальное значение: "))):
    if el > 10:
        break
    else:
        print(el)
print("Ввод завершен")

#b
list = []
i = 0
for el in cycle(["a", "b", "c", "d", "e"]):
    if i > 10:
        break
    print(el)
    i += 1
