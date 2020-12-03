def func(*args):
    return args

num1 = float(input('Введите делимое число: '))
num2 = float(input('Введите делитель: '))
if num2 != 0:
   print(func(num1, 'делим на', num2, 'разность =', num1/num2))
elif num2 == 0:
   print('На 0 делить нельзя!')