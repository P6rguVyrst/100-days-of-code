
class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

x = AlwaysBlueCar('green', 12345).color
print(x)

def print_vector(x, y, z):
    print('<{}, {}, {}>'.format(x,y,z))

a = (1, 2, 4)
b = {'x': 1, 'y': 2, 'z': 6}

print_vector(*a)
print_vector(**b)



