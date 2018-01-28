

class ManagedFile:


    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('test.txt') as f:
    f.write('hello world!\n')
    f.write('bye now\n')


from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('crazy stuff happens\n')
    f.write('in crazytown\n')




class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)



with Indenter() as indent:
    indent.print('alpha')
    with indent:
        indent.print('bravo')
        with indent:
            indent.print('charlie')
    indent.print('delta')

