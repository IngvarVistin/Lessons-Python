from os import remove
with open('plan&plan.txt', 'w') as f:
    f.write('Информатика: 100(л) 50(пр) 210(лаб)\nФизика: 30(л) 0(пр) 10(лаб)\nФизкультура: 0(л) 30(пр) 0(лаб)')
dict_ = {}
with open('plan&plan.txt') as f:
    list_ = f.read().split('\n')
    for line in list_:
        line = line.split()
        subj, lect, pract, lab = line
        dict_[subj] = int(lect[:-3]) + int(pract[:-4]) + int(lab[:-5])
    print(f'Общее количество часов по предметам - \n {dict_}')
remove('plan&plan.txt')
