from itertools import count
from math import factorial
def seq():
    for el in count(num):
        yield factorial(el)
num = int(input('Введите число для начала расчёта: '))
num_fin = int(input('Введите число до которого производить расчёт: '))
gen = seq()
x = 0
for i in gen:
    if x < num_fin:
        print(i)
        x = x + 1
    else:
        break
