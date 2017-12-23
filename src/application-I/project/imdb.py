import re
from time import time
import json
import requests
from pprint import pprint as pp
from imdbpie import Imdb

class ImdbFilter(object):

    def __init__(self):
        self.imdb = Imdb(anonymize=True)

    def imdb_search_for_title(self, title):
        uri = 'http://www.imdb.com/title'
        search_result = self.imdb.search_for_title(title['title'])
        results = self.filter_title(search_result, title)
        for item in results:
            item['uri'] = f'{uri}/{item.get("imdb_id")}/'
            t = self.imdb.get_title_by_id(item.get('imdb_id'))
            if t:
                item['type'] = t.type
                item['tagline'] = t.tagline
                item['rating'] = t.rating
                item['genres'] = t.genres
                item['votes'] = t.votes
                item['runtime'] = t.runtime
                item['creators'] = t.creators
                if item['runtime']:
                    item['runtime'] /= 60
        return results

    def filter_title(self, search_result, title):
        matches = []
        for item in search_result:
            if str(item['title'].upper()) == str(title['title'].upper()):
                if item['year']:
                    if str(item['year']) == str(title['year']):
                        matches.append(item)
                else:
                    matches.append(item)
        return matches

p = ImdbFilter()


def extract_year(title):
    pattern = '(.*?)( \d{4}?)'
    movies = re.compile(pattern)
    year_match = re.search(movies, title.upper())
    if year_match:
        x = str(year_match[0]).split(' ')
        data = dict(
            title = ' '.join(x[:-1]),
            year = int(x[-1:][0]),
        )
    else:
        data = dict(
            title = title,
            year = None,
        )
    return data

def structure_data(data):
    result = {'media': []}
    print('Structuring data...')
    for key, value in data.items():
        tmp = {key: []}

        data = {key: [extract_year(x) for x in value]}
        for item in data[key]:
            item['imdb'] = p.imdb_search_for_title(item)
            tmp[key].append(item)
        result['media'].append(data)
    return result



def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
        f.close

def explore():

    titles = {
        'movies': {
            #'CAPTAIN AMERICA CIVIL WAR 2016',
            'INGRID GOES WEST 2017',
            'ONCE UPON A TIME IN AMERICA 1984',
        },
        'series': {
            'RICK AND MORTY',
            'SOUTH PARK',
            'ARCHER',
            'HOUSE OF CARDS',
        },
    }

    start = time()
    result = structure_data(titles)
    end = time()
    pp(result)
    elapsed = end-start
    print(f'Runtime: {elapsed}s')
    write_to_file('media.json', json.dumps(result))


explore()
