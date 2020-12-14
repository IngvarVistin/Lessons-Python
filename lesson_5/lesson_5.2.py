from os import remove
with open('Jonathan Seagull.txt', 'w') as f:
    f.write('Он понимал, что это триумф!\nПредельная скорость! \nДвести четырнадцать миль в час для чайки! \nЭто был прорыв, незабываемый, неповторимый миг в истории Стаи и начало новой эры в жизни Джонатана.')
with open('Jonathan Seagull.txt') as f:
    print(f'Содержимое файла: \n{f.read()}')
with open('Jonathan Seagull.txt') as f:
    print(f'Количества строк в файле: {len(f.readlines())}')
with open('Jonathan Seagull.txt') as f:
    content = f.readlines()
    for i in range(len(content)):
        print(f'Количество символов {i+1} строки: {len(content[i])}')
with open('Jonathan Seagull.txt') as f:
    content = f.read().split()
    print(f'Количество слов в файле: {len(content)}')
remove('Jonathan Seagull.txt')