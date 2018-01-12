#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import functools


class lazy_property(object):

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        relatives = 'Many relatives.'
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return 'Father and mother'


def main():
    John = Person('Jhon', 'Coder')
    print(u'Name: {0} Occupation: {1}'.format(John.name, John.occupation))
    print(u'Before we access "relatives":')
    print(John.__dict__)
    print(u'John\'s relatives: {0}'.format(John.relatives))
    print(u'After we\'ve accessed "relatives":')
    print(John.__dict__)
    print(John.parents)
    print(John.__dict__)
    print(John.parents)
    print(John.call_count2)


if __name__ == '__main__':
    main()


