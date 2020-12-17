class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'{self.title} - Запуск отрисовки'
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title} - Запуск отрисовки'
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title} - Запуск отрисовки'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'{self.title} - Запуск отрисовки'

Pen = Pen('Ручка')
Pencil = Pencil('Карандаш')
Handle = Handle('Маркер')
print(Pen.draw())
print(Pencil.draw())
print(Handle.draw())