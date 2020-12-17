class Car:
    def __init__(self, name, is_polise, speed, color):
        self.name = name
        self.is_polise = is_polise
        self.speed = speed
        self.color = color
    def go(self):
        return f'Автомобиль {self.name} начал движение.'
    def stop(self):
        return f'Автомобиль {self.name} начал движение.'
    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево.'
    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо.'
    def show_speed(self):
        return f'Автомобиль {self.name} движется со скоростью {self.speed}.'

class TownCar(Car):
    def __init__(self, name, is_polise, speed, color):
        super().__init__(name, is_polise, speed, color)
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} движется со скорстью {self.speed} превышает скорость на {self.speed - 60}.'
        else:
            return f'Автомобиль {self.name} движется с разрешённой скоростью.'

class SportCar(Car):
    def __init__(self, name, is_polise, speed, color):
        super().__init__(name, is_polise, speed, color)

class WorkCar(Car):
    def __init__(self, name, is_polise, speed, color):
        super().__init__(name, is_polise, speed, color)
    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} движется со скорстью {self.speed} превышает скорость на {self.speed - 40}.'
        else:
            return f'Автомобиль {self.name} движется с разрешённой скоростью.'

class PoliceCar(Car):
    def __init__(self, name, is_polise, speed, color):
        super().__init__(name, is_polise, speed, color)

TAXI = TownCar('TAXI', False, 50,'Yellow')
Ferrari = SportCar('Ferrari', False, 180, 'Red')
MAN = WorkCar('MAN', False, 80, 'Grey')
Bugatty = PoliceCar('Bugatty', True, 200, 'Ultramarine')

print(TAXI. go())
print(Ferrari. go())
print(MAN. go())
print(Bugatty. go())

print(TAXI. turn_right())
print(Ferrari. show_speed())
print(MAN. turn_left())
print(MAN.show_speed())
