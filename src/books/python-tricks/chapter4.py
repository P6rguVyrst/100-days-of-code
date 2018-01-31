from exceptions import (
    BaseValidationError,

)

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

def validate(name):
    if len(name) < 10:
        raise NameTooShortError

try:
    print(validate('Toomas'))
except BaseValidationError as e:
    print(e)
