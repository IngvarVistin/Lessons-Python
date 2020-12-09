list = [3, 3, 3, 8, 34, 2, 55, 55, 4, 3, 21, 8, 5, 22]
new_list = [el for el in list if list.count(el) < 2]
print(new_list)