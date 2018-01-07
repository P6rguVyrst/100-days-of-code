import pytest
from src.atm import ATM

class TestATM(object):

    @pytest.fixture(scope='module')
    def app(self):
        return ATM()

    def test_catch_counterfit(self):
        pass

    def test_money_left(self, app):
        assert app.money_left() == app.balance

    def test_bills_left(self, app):
        bills_left = app.bills_left()
        assert isinstance(bills_left, dict)
        assert bills_left == app.b

    def test_bills(self):
        pass

    def test_whidraw(self, app):
        whidrawl = app.whidraw(200)
        assert whidrawl
        assert isinstance(whidrawl, dict)

    def test_whidraw_fail(self, app):
        gibberish = [
            'money', 1.01, 1.00, 0x13, # 0x13 fails int 19
            b'\x13\xff\x00\x00\x08\x00',

        ]
        for foo in gibberish:
            with pytest.raises(AssertionError):
                print(foo)
                app.whidraw(foo)


    def test_deposit(self):
        pass
