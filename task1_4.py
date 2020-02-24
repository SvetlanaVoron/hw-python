# Задание 4
number = int(input('Введите целое положительное число: '))
max = 0
figure = number
while figure > 0:
    x = figure % 10
    if x > max:
        max = x
    figure = figure // 10
print('Наибольшая цифра у введенного числа:', max)



