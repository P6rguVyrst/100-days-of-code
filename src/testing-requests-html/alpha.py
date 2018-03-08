from requests_html import HTMLSession
from pprint import pprint as pp
skyscanner_uri = 'https://www.skyscanner.net/transport/flights/tll/lond?adults=1&children=0&adultsv2=1&childrenv2&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1803&iym=1804&ref=home&selectedoday=23&selectediday=04'
session = HTMLSession()
skyscanner = session.get(skyscanner_uri)
#pp(skyscanner.html.links)
#pp(skyscanner.html.absolute_links)
content = skyscanner.html.find('#content', first=True)
pp(content.text)

