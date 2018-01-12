
class Dog(object):

    def speak(self):
        return 'Woof!'

    def __str__(self):
        return 'Dog'

class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return 'Dog food...'
