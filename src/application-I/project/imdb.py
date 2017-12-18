
import requests
from pprint import pprint as pp

class Paths(object):
    """
    https://stackoverflow.com/questions/1966503/does-imdb-provide-an-api
        http://www.imdb.com/interfaces/#plain
        http://app.imdb.com/title/maindetails?tconst=tt0382932

    """

    def __init__(self):
        self.api = 'http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q='

    def make_name_search_uri(self, search_title):
        search_string = self.make_search_string(search_title)
        uri = f'http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q={search_string}'
        return uri

    def make_search_string(self, search_title):
        search_string = search_title.replace(' ', '+')
        return search_string

    def search_title(self, uri):
        r = requests.get(uri).json()
        return r


