
class TC1(object):

    def run(self):
        print('Runing test 1')


class TC2(object):

    def run(self):
        print('Runing test 2')


class TC3(object):

    def run(self):
        print('Runing test 3')


#Facade
class TestRunner(object):

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]

if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

