class Cell:
    def __init__(self, quant_cell):
        self.quant_cell = int(quant_cell)

    def __str__(self):
        return f'Количество клеток - {self.quant_cell * "*"}'

    def __add__(self, other):
        return f'Результат операции сложения - {Cell(self.quant_cell + other.quant_cell)}'

    def __sub__(self, other):
        if (self.quant_cell - other.quant_cell) < 1:
            return f'Результат операции вычитания - {Cell(int(self.quant_cell - other.quant_cell))}'
        else:
             return f'Операция вычитания невозможна'

    def __mul__(self, other):
        return f'Результат операции умножения - {Cell(int(self.quant_cell * other.quant_cell))}'

    def __truediv__(self, other):
        return f'Результат операции деления - {Cell(round(self.quant_cell // other.quant_cell))}'


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quant_cell / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quant_cell % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells2)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(3))
print(cells1.make_order(6))
print(cells1 / cells2)