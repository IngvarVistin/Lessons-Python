from functools import reduce
def func(prev_el, el):
    return prev_el * el
print(f'Список четных чисел {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Произведение списка {reduce(func, [el for el in range(100, 1001) if el % 2 == 0])}')