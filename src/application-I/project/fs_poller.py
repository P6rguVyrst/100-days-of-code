#!/usr/bim/env python3
# -*- coding: utf-8 -*-

from os import walk
from pprint import pprint as pp
import re
import click
import json
import requests

# TODO:
#   Filter unique titles
#   Check unique titles in IMDB, RottenTomatoes, Youtube for trailers


class Definitions(object):

    def movies(self, filename):
        # Can only be identified by metadata (imdb, google etc...)
        pattern = '(.*?)( \d{4}?)|$'
        #pattern = '(.*?)\d{4}|$'
        movies = re.compile(pattern)
        year_match = re.search(movies, filename.upper())

        if not self.series(filename):
            if year_match:
                match = year_match[0]
                if match:
                    x = str(year_match[0]).split(' ')
                    data = dict(
                        title = ' '.join(x[:-1]),
                        year = int(x[-1:][0]),
                    )
                    return data

    def series(self, filename):
        pattern = '(.*)S\d{2}E\d{2}.*'
        series = re.compile(pattern)
        episode_match = re.findall(series, filename.upper())
        if episode_match:
            return dict(title=episode_match[0])


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


class WebScraper(object):

    def imdb(*args):
        pass


    def youtube(*args):
        pass


def unique_titles(videos, datatype):

    define = Definitions()

    options = {
        'series': define.series,
        'movies': define.movies,
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
                data['titles'].append(str(m))

    return data


def send_data(data):
    pp(data)
    uri = 'http://127.0.0.1:5000/notify'
    extra = {'msg_type': 'media'}
    d = {**data, **extra}
    #r = requests.post(uri, data=json.dumps(d))
    #print(json.dumps(d))


def get_year():
    return 2018

def get_imdb():
    return 'https://www.imdb.com'

def get_trailer():
    return 'trailer'

def alpha(media_list):
    data = []
    for title in media_list:
        #item = dict(
        #    title = title,
        #    #year = get_year(),
        #    #imdb = get_imdb(),
        #    #trailer = get_trailer(),
        #)
        data.append(title)

    return data


@click.command()
@click.option('--home', prompt='Root directory', help='Root directory to scrape for files')
def main(home):

    filetypes = ['.mkv', '.avi', '.mp4']
    fsd = FSDiscovery()
    videos = fsd.discover_rawdata(filetypes, home)

    # set() for uniq
    movies = unique_titles(videos, 'movies')
    series = unique_titles(videos, 'series')

    uniq_movies = list(set(movies['titles']))
    uniq_series = list(set(series['titles']))

    payload = {
        'movies': alpha(uniq_movies),
        'series': alpha(uniq_series),
    }

    send_data(payload)


if __name__ == '__main__':
    main()
