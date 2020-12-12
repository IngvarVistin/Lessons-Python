with open('text.txt', 'w') as f:
    list = input('Введите текст для записи в файл: ')
    while list:
        f.write(list + '\n')
        list = input('Введите текст для записи в файл: ')
        if not list:
            break
with open('text.txt') as f:
     text = f.read()
     print(text)