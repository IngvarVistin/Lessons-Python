def my_func(arg_1, arg_2, arg_3):
    if arg_3 <= arg_1 and arg_2:
        return arg_1 + arg_2
    elif arg_2 <= arg_1 and arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3

print(f"result - {my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Введите третий аргумент: ')))}")
