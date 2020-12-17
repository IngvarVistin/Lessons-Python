class Worker(object):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
       return '{} {}'.format(self.name, self.surname)
    def get_total_income(self):
       return self._income["wage"] + self._income["bonus"]

pos = Position('Иван', 'Петров', 'Слесарь', 50000, 20000)
print(f'Полное имя: {pos.get_full_name()}')
print(f'Должность: {pos.position}')
print(f'Доход с учётом премии: {pos.get_total_income()}')
