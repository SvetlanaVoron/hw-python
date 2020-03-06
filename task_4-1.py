# Задание 1
from sys import argv

script_name, h, a, bonus = argv
amount = int(h) * int(a) + int(bonus)

print("Имя скрипта: ", script_name)
print("Сумма заработной платы: ", amount)

# включить проверку ошибок
