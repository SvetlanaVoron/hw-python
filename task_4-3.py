# Задание 3
#v1
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

#v2
from itertools import count

for el in count(20):
    if el > 240:
        break
    else:
        if el % 20 == 0 or el % 21 == 0:
            print(el)

#