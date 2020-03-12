# Задание 6 +
dict_lesson = {}
with open("Text6.txt", "r") as f_lessons:
    line = f_lessons.read().split("\n")
    for i in line:
        lesson, content = i.split(": ")
        type_list = content.split(" ")
        new_list = []
        #print(i)
        #print(type_list)
        for el in type_list:
            if el != "-":
                new_list.append(el)
        sum_list = []
        for el in new_list:
            el = el.split("(")
            sum_list.append(int(el[0]))
        dict_lesson[lesson] = sum(sum_list)
    print(dict_lesson)