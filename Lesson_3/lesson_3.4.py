# Первый вариант решения

def my_func(x, y):
    return x**y
print(f"{my_func(float(input('Введите действительное число: ')), int(input('Введите целое отрицательное число: ')))}")



# Второй вариант решения
'''
def my_func(x, y):
    n = 0
    m = 1
    while n < abs(y):
        m = m * (1/x)
        n = n+1
    else:
        return (m)
print(f"{my_func(float(input('Введите действительное число: ')), int(input('Введите целое отрицательное число: ')))}")
'''