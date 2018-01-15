import time


class SalesManager(object):
    def talk(self):
        print('Sales manager')

class Proxy(object):
    def __init__(self):
        self.busy = 'no'
        self.sales = None

    def talk(self):
        print('Proxy chcking for sales manager availability')

        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleet(0.5)
            self.sales.talk()
        else:
            time.sleep(1)
            print('Sales manager is busy')

class NoTalkProxy(Proxy):
    def talk(self):
        print('Checking for sales manager availability')
        time.sleep(0.3)
        print('The sales manager will not talk to you.')

if __name__ == '__main__':

    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

