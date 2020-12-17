class Road:
    _length = int(input('Введите длину дороги в метрах: '))
    _width = int(input('Введите ширину дороги в метрах: '))
    def __init__(self):
        Road._length = self._length
        Road._width = self._width
        self._mass = int(input('Введите массу (кг) асфальта, площадью 1 кв м. и высотой 5 см.: '))
        self._thick = int(input('Введите необходимую толщину асфальта (см): '))
    def asphalt(self):
        return self._length * self._width * self._mass * self._thick

Road = Road()
print(f'Для покрытия всего дорожного полотна необходимо {Road.asphalt()} кг асфальта')

