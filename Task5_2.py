# Задание 2 +
f = open("Text2.txt", "r")
str = f.readlines()
print(str)
print(f"Количество строк: {len(str)}")

for i, str in enumerate(str, start=1):
    words = len(str.split())
    print(f"В строке №{i}: количество слов: {words}")
f.close()