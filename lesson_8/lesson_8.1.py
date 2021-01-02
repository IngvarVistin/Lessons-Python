class Data:
    def __init__(self, data_str):
        self.data_str = str(data_str)

    @classmethod
    def extract(cls, data_str):
        my_date = []
        for i in data_str.split('-'):
            my_date.append(i)
        return (my_date[0]), (my_date[1]), (my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.data_str)}'

today = Data('29-12-2020')
print(today)
print(Data.valid(2, 10, 2029))
print(today.valid(15, 17, 2019))
print(Data.extract('15-12-2011'))
print(today.extract('2-1-2020'))
print(Data.valid(1, 11, 2000))