
class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print('This is a lovely {}'.format(pet))
        print('It says {}'.format(pet.speak()))
        print('It eats {}'.format(self.pet_factory.get_food()))

