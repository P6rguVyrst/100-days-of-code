

class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return f'a {self.color} car __str__'

    def __repr__(self):
        return '__repr__ for Car'


c = Car('blue', 123)
print(c)
print(repr(c))


