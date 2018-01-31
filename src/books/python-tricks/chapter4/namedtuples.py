from collections import namedtuple

Car = namedtuple('Car',[
    'color',
    'milage',

])

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


mycar = Car('orange', 666)
#print(mycar.color)
#print(mycar.milage)
#print(tuple(mycar))
a, b = mycar
print(a, b)
print(mycar)

c = MyCarWithMethods('red', 123)
print(c.hexcolor())


ElectricCar = namedtuple(
    'ElectricCar', Car._fields + ('charge',)
)
print(ElectricCar('red', 1234, 12.22))
import json
print(mycar._asdict())
x = json.dumps(mycar._asdict())
print(x)



