# Задача 3 +
with open("Text3.txt") as f:
    list_salary = []
    str = f.read().split("\n")
    list_above = []
    for el in str:
        el = el.split()
        if float(el[1]) < 20000:
            list_above.append(el[0])
        list_salary.append(float(el[1]))
        average_sal = sum(list_salary)/len(list_salary)
    print(f"ФИО с ЗП ниже 20000 - {list_above}, средняя ЗП = {average_sal}" )