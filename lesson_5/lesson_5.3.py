from os import remove
with open("salaries&empl.txt", 'w') as f:
    f.write("Иванов 12000\nПетров 18000\nСидоров 16000\nАлексеев 21000")
with open("salaries.txt") as f:
    list_empl = []
    sal = []
    empl = f.read().split('\n')
    for i in empl:
        i = i.split()
        if int(i[1]) < 20000:
            list_empl.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20 тыс. у сотрудников: {list_empl}\nСредний оклад: {sum(map(int,sal))/len(sal)}')
remove('salaries&empl.txt')