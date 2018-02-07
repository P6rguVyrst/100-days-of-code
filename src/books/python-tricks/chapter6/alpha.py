from time import sleep


my_items = ['a', 'b', 'd']

for i, item in enumerate(my_items):
    print(f'{i}: {item}')

'''
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        sleep(1)
        return self.source.value

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)
'''
class Repeater:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        sleep(1)
        return self.value

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater('Hello!', 5)

for item in repeater:
    print(item)


# Generators and Generator expressions

def repeater(value):
    while True:
        sleep(1)
        yield value

def bounded_repeater(value, max_repeats):
    for v in range(max_repeats):
        yield value

for i in bounded_repeater('lsd', 3):
    print(i)

iterator = ('hi' for i in range(3))
for i in iterator:
    print(i)
#for i in repeater('heh'):
#    print(i)


