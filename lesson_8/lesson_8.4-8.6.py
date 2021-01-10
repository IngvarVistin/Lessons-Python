class StorageTechnique:

    def __init__(self, name, price, quantity, number_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_lists
        self.my_storage_full = []
        self.my_storage = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit_name = input(f'Введите наименование: ')
            unit_price = int(input(f'Введите цену за ед: '))
            unit_quant = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit_name, 'Цена за ед': unit_price, 'Количество': unit_quant}
            self.my_unit.update(unique)
            self.my_storage.append(self.my_unit)
            print(f'Текущий список -\n {self.my_storage}')
        except:
            return f'Ошибка ввода!'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_storage_full.append(self.my_storage)
            print(f'Весь склад -\n {self.my_storage_full}')
            return f'Выход'
        else:
            return StorageTechnique.reception(self)


class Printer(StorageTechnique):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StorageTechnique):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StorageTechnique):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 5000, 5, 10)
unit_2 = Scanner('Canon', 4500, 5, 10)
unit_3 = Copier('Xerox', 3200, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())