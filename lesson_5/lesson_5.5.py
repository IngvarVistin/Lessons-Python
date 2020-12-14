from os import remove
with open('text&nums.txt', 'w') as f:
    f.write(input('Введите набор чисел, разделённых пробелами: '))
with open('text&nums.txt') as f:
    numb = f.read().split()
    print(f'Сумма всех чисел: {sum(map(int, numb))}')
remove('text&nums.txt')