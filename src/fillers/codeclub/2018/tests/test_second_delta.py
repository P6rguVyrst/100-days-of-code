from codeclub.second.delta import ATM

def test_atm_init(atm):
    atm = ATM(fives=1000, tens=500, twenties=250,
              fifties=100, hundreds=50,
              thundreds=25, fhundreds=10)
    for key, value in atm.b.items():
        assert key*value == 5000

    atm = ATM(fives='asd', tens=-1, twenties='',
              fifties='', hundreds='123',
              thundreds=-1000, fhundreds=None)
    for key, value in atm.b.items():
        print(key, value)
        assert key*value == 0

def test_whidraw1(atm):
    whidraw = atm.whidraw_sum(500)
    print(whidraw)

def test_whidraw_500(atm):
    bills = atm.b
    whidraw = atm.whidraw_sum(500)
    assert whidraw[200] == 2
    assert whidraw[50] == 2

def test_whidraw_100(atm):
    whidraw = atm.whidraw_sum(100)
    print(whidraw)
    assert whidraw[50] == 2

def test_whidraw_750(atm):
    whidraw = atm.whidraw_sum(750)
    print(whidraw)
    assert whidraw[500] == 1
    assert whidraw[200] == 1
    assert whidraw[20] == 2
    assert whidraw[5] == 2


def test_whidraw(atm):
    whidraw = atm.whidraw_sum(71)

    for k, v in whidraw.items():
        assert isinstance(k, int)
        assert v == 0
    whidraw = atm.whidraw_sum(36000)
    for v in whidraw.values():
        assert v == 0

    print(whidraw)


class TestATM():

    def test_money_left(self):
        pass

    def test_bills_left(self, atm):
        bills = atm.bills_left()
        assert isinstance(bills, dict)
        money_left = lambda: sum(k*v for k, v in bills.items())
        assert money_left() == 35000


    def test_whidraw(self):
        pass

    def test_deposit(self):
        pass

