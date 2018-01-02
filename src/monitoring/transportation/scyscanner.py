
# Scyscanner seems to be blocking robots.
# Can't site access searches directly - need to use real browser drivers.
# Seems it can only be done with selenium.

class URIFactory(object):

    def __init__(self):
        base = 'https://www.skyscanner.net'
        category = 'transport'
        method = 'flights'
        self.base_flights = f'{base}/{category}/{method}'


    def flights(self):
        return self.base_flights



    #def flights(self):

    ##    'https://www.skyscanner.net/transport/flights/rix/lond?adults=1&children=0&adultsv2=1&childrenv2&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&oym=1801&selectedoday=01&iym=1801&selectediday=01'

    # https://www.skyscanner.net/transport/flights/rix/ltn?adults=1&children=0&adultsv2=1&childrenv2&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&oym=1803&selectedoday=01&iym=1803&selectediday=01


class ScyScanner(object):

    def __init__(self):
        self.base_uri = URIFactory()
        self.return_ticket = True
        self.starting_point = 'None'
        self.destination = None
        self.depart_date = None
        self.return_date = None
        self.cabin_class = 'Economy'
        self.adults = 1

    def find_flight(self):

        flights = self.base_uri.flights()
        x = f'{flights}/{self.starting_point}/{self.destination}?adults={self.adults}&'
        print(x)


