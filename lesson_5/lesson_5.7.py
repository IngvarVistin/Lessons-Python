import json
from os import remove
with open('firm&firm.txt', 'w') as f:
    f.write('firm_1 ООО 10000 5000\nfirm_2 OAO 15000 7000\nfirm_3 OOO 10000 12000')
dict_prof = {}
dict_ave_prof = {}
av_prof = []
list_firms = [dict_prof, dict_ave_prof]

with open('firm&firm.txt') as f:
    lines_f = f.readlines()
    for i in lines_f:
        i = i.split()
        firm, prop, rev, cost = i
        rev = int(rev)
        cost = int(cost)
        prof = rev - cost
        dict_prof[firm] = prof
        if prof > 0:
            av_prof.append(prof)
        dict_ave_prof['average_profit'] = round((sum(map(int, av_prof))/len(lines_f)), 2)
# print(list_firms)
with open('firm&firm.json', 'w', encoding='utf-8') as f:
    json.dump(list_firms, f)
with open('firm&firm.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(result)

remove('firm&firm.txt')
remove('firm&firm.json')
