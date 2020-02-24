# Задание 6

distance = int(input(" Результат пробежки в 1-й день, км: "))
goal_distance = int(input(" Целевой результат пробежки, км: "))
day = 1

while distance < goal_distance:
    distance *= 1.1
    day += 1
    print(f'День тренировки {day}-й: ' + 'дистанция %.2f' % (distance) + ' км')
if distance >= goal_distance:
    print(f"Результат достигнут на {day}-й день")
