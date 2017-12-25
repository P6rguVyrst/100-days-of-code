# -*- coding: utf-8 -*-

from os import walk
from pprint import pprint as pp
import re
import json
import click




class FSDiscovery(object):

    def __init__(self):
        pass

    def discover_rawdata(self, filetypes, home):
        payload = {'data': []}
        for (dirpath, dirnames, filenames) in walk(home):
            hit = [f for f in filenames if f.endswith(tuple(filetypes))]
            if hit:
                payload['data'].append({'folder': {'files': hit, 'path': dirpath}})
        return payload

    def filter_series(self, disco):
        d = Definitions()
        series = []
        for item in disco['data']:
            files = item['folder']['files']
            for name in files:
                if d.series(name):
                    series.append(name)
        return series


class Media(object):

    def unique_titles(self, videos, datatype):
        options = {
            'series': self.series,
            'movies': self.movies,
        }
        data = {'titles': []}
        for title in videos['data']:
            for f in title.get('folder', {}).get('files'):
                f = f.replace('.', ' ')
                f = f.replace('-', ' ')
                f = f.replace(' ', ' ')
                #Handle errors
                m = options[datatype](f)
                if m:
                    data['titles'].append(m)
        return data

    def movies(self, filename):
        pattern = '(.*?)( \d{4}?)'
        #pattern = '(.*?)\d{4}|$'
        movies = re.compile(pattern)
        year_match = re.search(movies, filename.upper())
        if not self.series(filename):
            if year_match:
                return year_match[0]
                #match = year_match[0]
                #if match:
                #    return match
                    #x = str(year_match[0]).split(' ')
                    #data = dict(
                    #    title = ' '.join(x[:-1]),
                    #    year = int(x[-1:][0]),
                    #)
                    #pp(data)
                    #return data

    def series(self, filename):
        pattern = '(.*)S\d{2}E\d{2}.*'
        series = re.compile(pattern)
        episode_match = re.findall(series, filename.upper())
        if episode_match:
            return episode_match[0].rstrip()


def send_data(data):
    pp(data)
    uri = 'http://127.0.0.1:5000/notify'
    extra = {'msg_type': 'media'}
    d = {**data, **extra}
    #r = requests.post(uri, data=json.dumps(d))
    #print(json.dumps(d))



@click.command()
@click.option('--home', prompt='Root directory', help='Root directory to scrape for files')
def main(home):

    filetypes = ['.mkv', '.avi', '.mp4']

    fsd = FSDiscovery()
    videos = fsd.discover_rawdata(filetypes, home)

    media = Media()
    movies = media.unique_titles(videos, 'movies')
    series = media.unique_titles(videos, 'series')
    uniq_movies = list(set(movies['titles']))
    uniq_series = list(set(series['titles']))

    payload = {
        'movies': uniq_movies,
        'series': uniq_series,
    }
    send_data(payload)



if __name__ == '__main__':
    main()
