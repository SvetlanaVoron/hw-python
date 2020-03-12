# Задание 4 +
num_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("Texе4_rus.txt", "w") as f_rus:
    with open("Texе4.txt", "r") as f_eng:
        line = f_eng.read().split("\n")
        for i in line:
            i = i.split(" - ")
            f_rus.writelines(num_dict[i[0]] + ' - ' + i[1] + "\n")

with open("Texе4_rus.txt", "r") as f_rus:
    print(f_rus.read())