class Dog(object):


    def __init__(self):
        self.name = 'Dog'

    def bark(self):
        return 'Woof!'


class Cat(object):


    def __init__(self):
        self.name = 'Cat'

    def meow(self):
        return 'Meow!'


class Human(object):


    def __init__(self):
        self.name = 'Adam'

    def speak(self):
        return 'Hello world!'


class Car(object):


    def __init__(self):
        self.name = 'Car'

    def make_noise(self, octane_level):
        return 'vroom{0}'.format('!' * octane_level)


