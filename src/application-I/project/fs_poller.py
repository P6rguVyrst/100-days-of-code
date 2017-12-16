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
        pattern = '(.*)( \d{4}?)|$'
        movies = re.compile(pattern)
        year_match = re.search(movies, filename.upper())
        if year_match:
            # FIXIT: Series pattern "S0630" also matched
            if not self.series(filename):
                # FIXIT
                return year_match[0]

    def series(self, filename):
        pattern = '(.*)S\d{2}E\d{2}.*'
        series = re.compile(pattern)
        episode_match = re.findall(series, filename.upper())
        if episode_match:
            return episode_match[0]


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
    # Google search for first title + imdb. imdb hit. - imdb id?
    # search for movies: https://www.omdbapi.com/ - search by imdbid?
    # need to filter down titles better.
    """
    OMDB Data sample:

    {"Title":"Guardians of the Galaxy Vol. 2","Year":"2017","Rated":"PG-13","Released":"05 May 2017","Runtime":"136 min","Genre":"Action, Adventure, Sci-Fi","Director":"James Gunn","Writer":"James Gunn, Dan Abnett (based on the Marvel comics by), Andy Lanning (based on the Marvel comics by), Steve Englehart (Star-lord created by), Steve Gan (Star-lord created by), Jim Starlin (Gamora and Drax created by), Stan Lee (Groot created by), Larry Lieber (Groot created by), Jack Kirby (Groot created by), Bill Mantlo (Rocket Raccoon created by), Keith Giffen (Rocket Raccoon created by), Steve Gerber (Howard the Duck created by), Val Mayerik (Howard the Duck created by)","Actors":"Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel","Plot":"The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.","Language":"English","Country":"USA, New Zealand, Canada","Awards":"6 wins & 13 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"83%"},{"Source":"Metacritic","Value":"67/100"}],"Metascore":"67","imdbRating":"7.8","imdbVotes":"301,863","imdbID":"tt3896198","Type":"movie","DVD":"22 Aug 2017","BoxOffice":"$389,804,217","Production":"Walt Disney Pictures","Website":"https://marvel.com/guardians","Response":"True"}

    """
    # REGEXES TO MATCH: year, season
    # Match everything up to
    define = Definitions()

    #define.series()

    #print(m)
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

    #print(set(data['titles']))
    return data


def send_data(data):
    # pretty good filter, but not perfect
    pp(data)
    uri = 'http://127.0.0.1:5000/notify'
    extra = {'msg_type': 'media'}
    d = {**data, **extra}
    #r = requests.post(uri, data=json.dumps(d))
    print(json.dumps(d))


def get_year():
    return 2018

def get_imdb():
    return 'https://www.imdb.com'

def get_trailer():
    return 'trailer'

def alpha(media_list):
    data = []
    for title in media_list:
        item = dict(
            title = title,
            year = get_year(),
            imdb = get_imdb(),
            trailer = get_trailer(),
        )
        data.append(item)

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
