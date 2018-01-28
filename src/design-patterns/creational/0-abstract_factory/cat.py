
class Cat(object):

    def speak(self):
        return 'Meeeow!'

    def __str__(self):
        return 'Cat'

class CatFactory(object):

    def get_pet(self):
        return Cat()

    def get_food(self):
        return 'Cat food...'
