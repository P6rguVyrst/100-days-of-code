from objects import (
    Cat,
    Dog,
    Human,
    Car,
)

class Adapter(object):


    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())

    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))

    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))

    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print('A {0} goes {1}'.format(obj.name, obj.make_noise()))



if __name__ == '__main__':
    main()
