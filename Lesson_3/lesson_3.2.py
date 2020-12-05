def func(**kwargs):
5
    return kwargs

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите электронный адрес: ')
tel = input('Введите номер телефона: ')
print(func(Имя=name, Фамилия=surname, Год_рождения=year, Город_проживания=city, Электронный_адрес=email, Номер_телефона=tel))
