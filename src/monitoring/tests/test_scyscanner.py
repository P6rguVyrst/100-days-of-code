import requests
from transportation.scyscanner import ScyScanner, URIFactory


class TestURIFactory(object):

    def test_flights(self):
        app = URIFactory()
        assert app.flights() == 'https://www.skyscanner.net/transport/flights'



class TestScyScanner(object):


    def test_find_fligt(self):
        uri = 'https://www.skyscanner.net/transport/flights/rix/ltn?adults=1&children=0&adultsv2=1&childrenv2&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&oym=1803&selectedoday=01&iym=1803&selectediday=01'
        status_code = requests.get(uri).status_code
        assert status_code == 200
