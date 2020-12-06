def sum_total():
    symbol = False
    total = 0
    while symbol == False:
        numbers = input('Введите числа, разделённые пробелом, либо "the_end" для выхода: ').split()
        summ = 0
        for i in range(len(numbers)):
            if numbers[i] == 'the_end':
                symbol = True
                break
            else:
                summ = summ + int(numbers[i])
        total = total + summ
        print(total)
    print(f'Общай сумма равна {total}')
sum_total()