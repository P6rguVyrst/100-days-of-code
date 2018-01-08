import pytest
from src.atm import ATM

class TestATM(object):

    @pytest.fixture(scope='module')
    def app(self):
        """Test initialization."""
        test_atm = ATM()
        assert test_atm.balance == 35000
        atm = ATM(fives=1, tens=1, twenties=1, fifties=1,
                  hundreds=1, thundreds=1, fhundreds=1)
        return atm

    def test_catch_counterfit(self):
        pass

    #4 implemented
    def test_money_left(self, app):
        # assert int
        assert app.money_left() == app.balance

    #5 implemented
    def test_bills_left(self, app):
        bills_left = app.bills_left()
        assert isinstance(bills_left, dict)
        # assert bill int keys

        assert bills_left == app.b

    def test_bills(self):
        pass

    #6 - input
    #7 - output
    def test_whidraw(self, app):
        # assert whidraw int

        whidrawl = app.whidraw(200)
        assert whidrawl
        # assert keys are bill type int
        assert isinstance(whidrawl, dict)

    # 8 - give 0 if unable to whidraw
    def test_whidraw_fail(self, app):
        gibberish = [
            'money', 1.01, 1.00, #0x13, # 0x13 fails int 19
            #b'\x13\xff\x00\x00\x08\x00',

        ]
        for foo in gibberish:
            with pytest.raises(AssertionError):
                print(foo)
                app.whidraw(foo)

    #9
    def test_whidraw_logic(self):
        # return as big bills as possible
        # 1 tier bellow whidrawl ammount
        # 500 _> 2x200, 2x50
        pass


    #10
    def test_deposit(self):
       # input - dict, test bill types

        pass

    #2 implemented
    def test_bills_sum(self):
        # if value not set -> sum = 5000
        pass

    #3 implemented
    def test_catch_counterfit(self):
        # if incorrect -> 0
        pass





