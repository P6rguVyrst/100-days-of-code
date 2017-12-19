
import requests
from pprint import pprint as pp
from imdbpie import Imdb

class Paths(object):

    def __init__(self):
        self.imdb = Imdb(anonymize=True)

    def imdb_search_for_title(self, title):
        uri = 'http://www.imdb.com/title'
        search_result = self.imdb.search_for_title(title['title'])
        results = self.filter_title(search_result, title)
        for item in results:
            item['uri'] = f'{uri}/{item.get("imdb_id")}/'

        return results

    def filter_title(self, search_result, title):
        matches = []
        for item in search_result:
            if str(item['year']) == str(title['year']):
                if str(item['title'].upper()) == str(title['title'].upper()):
                    matches.append(item)
        return matches

    def make_search_string(self, search_title):
        search_string = search_title.replace(' ', '+')
        return search_string

    def search_title(self, uri):
        r = requests.get(uri).json()
        return r

#imdb = Imdb(anonymize=True)
p = Paths()

def explore():
    # Data needs to be cleaned a littl more
    titles = [
    #    'THE SPECTACULAR NOW',
    #    'THE DARK TOWER',
         {'title': 'LA LA LAND', 'year': 2016},
    #    'RICK AND MORTY ',
    #    'SOUTH PARK',
    #    'BOJACK HORSEMAN',
    ]
    for title in titles:
        x = p.imdb_search_for_title(title)
        #x = imdb.search_for_title(title)
        pp(x)

explore()
