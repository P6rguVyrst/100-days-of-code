import weakref

class FlyweightMeta(type):

    def __new__(mcs, name, parents, dct):
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance



class Card(object):

    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return '<Card: {}{}>'.format(self.value, self.suit)

def with_metaclass(meta, *bases):
    return meta('NewBase', bases, {})

class Card2(with_metaclass(FlyweightMeta)):

    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')

    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # tes tmetaclasses
    instances_pool = getattr(Card2, 'pool')
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 == cm2) != cm3
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0
