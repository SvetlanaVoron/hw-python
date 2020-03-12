# Задача 5 +
from random import randint

with open("Text5.txt", "w") as f_num:
    num_list = []
    for i in range(15):  # создание списка
        a = randint(0, 100)
        a = int(a)
        num_list.append(a)
    sum_list = sum([i for i in num_list ])
    f_num.write(f'Сумма сгенерированных чисел = {str(sum_list)}')
print(num_list)
with open("Text5.txt", "r") as f_num:
    print(f_num.read())

