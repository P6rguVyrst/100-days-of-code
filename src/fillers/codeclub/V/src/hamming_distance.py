
def get_distance(one, two):
    if len(one) != len(two):
        raise ValueError('Different length variables.')
    x = [str(bin(ord(x)))[2:] for x in one]
    y = [str(bin(ord(x)))[2:] for x in two]


