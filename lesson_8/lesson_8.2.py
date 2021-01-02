class exception:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @staticmethod
    def division_by_zero(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return (f"Деление на ноль недопустимо")

div = exception(10, 100)
print(exception.division_by_zero(10, 0))
print(exception.division_by_zero(100, 5))
print(div.division_by_zero(100, 0))