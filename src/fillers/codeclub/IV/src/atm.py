import inspect

class ATM(object):

    def __init__(self, fives=1000, tens=500, twenties=250,
                 fifties=100, hundreds=50,
                 thundreds=25, fhundreds=10):

        bills = self.catch_counterfit({
            5: fives,
            10: tens,
            20: twenties,
            50: fifties,
            100: hundreds,
            200: thundreds,
            500: fhundreds
        })
        self.b = bills
        self.balance = sum([k*v for k,v in bills.items()])


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
        if not isinstance(money, int):
            pass

        return

    def deposit(self): pass
