import random
from pet_shop import PetShop
from dog import DogFactory
from cat import CatFactory

def get_factory():
    options = [DogFactory(), CatFactory()]
    return random.choice(options)

shop = PetShop()

shop.pet_factory = get_factory()
shop.show_pet()

