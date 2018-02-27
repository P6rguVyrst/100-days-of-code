import binascii

def get_distance(one, two):
    assert len(one) == len(two)

x = get_distance(b'123', b'abc')
#x = get_distance('P', 'o')
print(x)
