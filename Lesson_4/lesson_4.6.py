from itertools import count, cycle
'''Задание "а" '''
start = int(input('Введите начальное число: '))
finish = int(input('Введите конечное число: '))
for el in count(start):
    if el > finish:
        break
    else:
        print(el)
'''Задание "б" '''
с = 0
fin = int(input('Введите число повторений: '))
for el in cycle(input("Введите элементы списка: ")):
    if с == fin:
        break
    print(el)
    с += 1
