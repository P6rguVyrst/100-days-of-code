

# SETS
vowels = {'a', 'e', 'i', 'o', 'u'}
print(type(vowels))

letters = set('toomas')
print(letters.intersection(vowels))
vowels.add('x')
print(vowels)

from collections import Counter
inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)
more_loot = {'sword': 1, 'apple': 2}
inventory.update(more_loot)
print(inventory)
#

# Queue - First In First Out
# Stack - Last In First Out


