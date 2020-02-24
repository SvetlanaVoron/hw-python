# Задание 5

value = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
fin_rez = value - costs
if fin_rez < 0:
    print('Вы работаете в убыток')
else:
    print('Ваша прибыль:', fin_rez)
    print("Ваша рентабельность: ", round((fin_rez/value)*100),'%')
    stuff = int(input('Укажиите численность персонала: '))
    print('Прибыль на 1 сотрудника составляет: %.2f' % (fin_rez/stuff))
