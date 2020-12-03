def func(*args):
    return args

num_1 = float(input('Введите делимое число: '))
num_2 = float(input('Введите делитель: '))
if num_2 != 0:
   print(func(num_1, 'делим на', num_2, 'разность =', num_1/num_2))
elif num_2 == 0:
   print('На 0 делить нельзя!')