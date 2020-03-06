#Задание 7
n = int(input("Укажите число: "))

def fact(n):
    x = 1
    for i in range(1, n+1):
        x *= i
        yield x

for y in fact(n):
        print([f'Факториал числа {n} = {y}'])


