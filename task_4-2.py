# Задание 2

from random import randint
list = []


for i in range(15):  # создание списка
    a = randint(0, 100)
    a = int(a)
    list.append(a)
print(list)

print([list[i] for i in range(len(list)) if list[i] > list[i - 1]]) # вывод значений

#