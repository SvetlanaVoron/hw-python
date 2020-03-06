# Задание 4

#без генератора
my_list = [1, 2, 1, 2, 5, 6, 13, 2]
my_set = set(my_list)
#print(my_set) - тестовая строка
new_list = list(my_set)
print(new_list)


#с генератором
from random import randint
my_list = []


for i in range(15):  # создание списка
    a = randint(0, 10)
    a = int(a)
    my_list.append(a)
print(my_list)

my_set = set(my_list)
#print(my_set) - тестовая строка
new_list = list(my_set)
print(new_list)


