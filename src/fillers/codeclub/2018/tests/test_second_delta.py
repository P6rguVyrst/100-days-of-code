from codeclub.second.delta import ATM

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

