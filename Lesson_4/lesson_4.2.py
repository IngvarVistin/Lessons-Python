from random import randint
list = []
for i in range(10):
    nomber = randint(1, 99)
    list.append(nomber)
new_list = [el for num, el in enumerate(list) if list[num-1]<list[num]]
print(list)
print(new_list)

