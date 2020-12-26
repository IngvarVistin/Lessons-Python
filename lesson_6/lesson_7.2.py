class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def expend_coat(self):
        return round((self.width / 6.5 + 0.5), 2)

    def expend_jacket(self):
        return round((self.height * 2 + 0.3), 2)

    @property
    def cloth_full(self):
        return str(f'Площадь ткани общая \n{round(((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)), 2)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round((self.width / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь на костюм {self.square_jacket}'

coat = Coat(3, 2)
jacket = Jacket(2, 1)
print(coat)
print(jacket)
print(coat.cloth_full)
print(jacket.cloth_full)
print(jacket.expend_coat())
print(jacket.expend_jacket())
