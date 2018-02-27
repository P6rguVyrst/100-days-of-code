import inspect


class Whidraw(object):


    def count_bills(self, whidraw_ammount):
        whidraw_bills = {
            5: 0,
            10: 0,
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0
        }

    def whidraw_sum(self, money):
        whidraw_bills = {
            5: 0,
            10: 0,
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0
        }
        bill_keys = [5, 10, 20, 50, 100, 200, 500]
        choices = len(bill_keys)
        try:
            assert money % 5 == 0
            s = 0
            while choices:
                bill = bill_keys[choices - 1]
                nr = money // bill
                if nr == 0:
                    choices -= 1
                elif nr == 1:
                    check = money - bill
                    if check == 0:
                        choices -= 1
                    else:
                        ammount = bill * nr
                        s += ammount
                        money -= ammount
                        whidraw_bills[bill] = nr
                    choices -= 1
                elif nr > 1:
                    ammount = bill * nr
                    s += ammount
                    money -= ammount
                    whidraw_bills[bill] = nr
        except AssertionError:
            pass

        return whidraw_bills

class ATM(Whidraw):

    def __init__(self, fives=1000, tens=500, twenties=250,
                 fifties=100, hundreds=50,
                 thundreds=25, fhundreds=10):

        # assert int for bills
        bills = self.catch_counterfit({
            5: fives,
            10: tens,
            20: twenties,
            50: fifties,
            100: hundreds,
            200: thundreds,
            500: fhundreds
        })
        self.b = bills # when money is whidrawn seld.b nust decrease.
        self.balance = sum([k*v for k,v in bills.items()])

    #TODO: simplify, make more easily testable
    def catch_counterfit(self, bills):
        for k, v in bills.items():
            try:
                if int(v) < 0:
                    bills[k]=0
            except ValueError:
                bills[k]=0
        return bills

    def money_left(self):
        return self.balance

    def bills_left(self):
        return self.b

    def bills(self): pass


    def whidraw(self, money):
        """
        The logic is that should be used for counting the bills for
        withdrawal is that if there is bill for exactly the amount
        that user wants (500) then the ATM should return bills that
        are tier below it (2x 200, 2x50). In case of 100 the bills
        given would be 2x50 and so on.
        Otherwise the largest possible bills should always be used.
        If user requests 750, then the ATM should return
        1x 500 and 1x200, 2x20 and 2x5
        """
        assert isinstance(money, int)
        payout = self.whidraw_sum(money)

        return payout



    def deposit(self, bills):
        assert isinstance(bills, dict)
        self.catch_counterfit(bills)

