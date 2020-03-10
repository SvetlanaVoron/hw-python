# Задание 1
with open("Text1.txt", "a+") as f:
    while True:
        str = input('Введите строку: ')
        if str == '':
            break
        f.write(str + "\n")
f = open("Text1.txt", "r")
content = f.read()
print(content)
f.close()


