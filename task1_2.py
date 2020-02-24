# Задание 2

time = int(input("Введите время в секундах: "))
h = time // 3600
min = time // 60 - h * 60
sec = time % 60
print(f'{h:02}:{min:02}:{sec:02}')