# Too tired to doo any real work - lets work on codeclub exericises.
# http://codeclub.thorgate.eu/challenges/124



def instruction_string(one, two):
    print('Move disk from {} pole to {} pole'.format(one, two))


def hanoi(N, source='starting', two='middle', dest='ending'):
    if N == 1:
        #instruction_string(one, two)
        instruction_string(one, three)
        if source:
            instruction_string(source, dest)
    else:
        N -= 1
        #instruction_string('middle', 'ending')
        hanoi(N, three,three, one)

x = hanoi(3)
print(x)


