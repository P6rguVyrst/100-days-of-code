from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    #def bar(self):
    #    pass

#b = Base()
#print(b.foo())
c = Concrete()
print(c.foo())

