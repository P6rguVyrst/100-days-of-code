
def get_distance(one, two):
    assert len(one) == len(two)
    xb = [str(bin(ord(x)))[2:] for x in one]
    yb = [str(bin(ord(x)))[2:] for x in two]


    i = sum(x != y for x, y in zip(xb, yb))
    print(i)

get_distance('ppp', 'abc')

