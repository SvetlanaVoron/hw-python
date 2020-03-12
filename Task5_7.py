# Задание 7 +
with open("Text7.txt", "r") as f_firms:
    f_line = f_firms.read().split("\n")
    result_list = []
    result_dict = {}
    for el in f_line:
        el = el.split(" ")
        result = int(el[2]) - int(el[3])
        result_list.append(result)
        result_dict[el[0]] = result
    #print(result_list)
    print(f"Финансовый результат компаний составляет, руб.: {result_dict}")
    profit_list = []
    for el in result_list:
        if el > 0:
            profit_list.append(el)
    #print(profit_list)
    average = sum(profit_list) / len(profit_list)
    print(f"Средняя прибыль {len(profit_list)} компаний c прибылью: {average:.2f} руб.")
    average_dict = {}
    average_dict['average'] = f"{average:.2f}"
    #print(average_dict)

import json

firms = [
    result_dict,
    average_dict
]

with open('firms_list.json', 'w', encoding='utf-8') as f_json:
    json.dump(firms, f_json, ensure_ascii=False, indent=4)



