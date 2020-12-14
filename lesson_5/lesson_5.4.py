from os import remove
with open("nomber&nombers.txt", 'w') as f:
    f.write("One — 1\nTwo — 2\nThree — 3\nFour — 4")
dict_ = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
list_ = []
with open("nomber&nombers.txt") as f:
    for i in f:
        i = i.split(' ', 1)
        list_.append(dict_[i[0]] + '  ' + i[1])
with open('nomber&nombers_2.txt', 'w') as f2:
    f2.writelines(list_)
with open('nomber&nombers_2.txt') as f3:
    print(f3.read())
remove('nomber&nombers.txt')
remove('nomber&nombers_2.txt')