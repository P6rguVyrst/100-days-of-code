import math


class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'



class Pizza:

    def __init__(self, radius, ingridients):
        self.radius = radius
        self.ingridients = ingridients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
            f'{self.ingridients!r})')

    @classmethod
    def margherita(cls):
        return cls(6, ['mozarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(6, ['mozarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

x = Pizza(6, ['cheese', 'tomatoes'])
y = Pizza.prosciutto()
print(x)
print(y)
