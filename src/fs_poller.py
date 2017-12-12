#!/usr/bim/env python3
# -*- coding: utf-8 -*-

from os import walk
from pprint import pprint as pp
import re
import click
import json

# TODO:
#   Filter unique titles
#   Check unique titles in IMDB, RottenTomatoes, Youtube for trailers


class Definitions(object):

    def movie(self):
        # Can only be identified by metadata (imdb, google etc...)
        pass

    def series(self, filename):
        pattern = '.*S\d{2}E\d{2}.*'
        series = re.compile(pattern)
        if series.match(filename):
            return True


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

def unique_titles(*args):
    # Google search for first title + imdb. imdb hit. - imdb id?
    # search for movies: https://www.omdbapi.com/ - search by imdbid?
    # need to filter down titles better.
    """
    OMDB Data sample:

    {"Title":"Guardians of the Galaxy Vol. 2","Year":"2017","Rated":"PG-13","Released":"05 May 2017","Runtime":"136 min","Genre":"Action, Adventure, Sci-Fi","Director":"James Gunn","Writer":"James Gunn, Dan Abnett (based on the Marvel comics by), Andy Lanning (based on the Marvel comics by), Steve Englehart (Star-lord created by), Steve Gan (Star-lord created by), Jim Starlin (Gamora and Drax created by), Stan Lee (Groot created by), Larry Lieber (Groot created by), Jack Kirby (Groot created by), Bill Mantlo (Rocket Raccoon created by), Keith Giffen (Rocket Raccoon created by), Steve Gerber (Howard the Duck created by), Val Mayerik (Howard the Duck created by)","Actors":"Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel","Plot":"The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.","Language":"English","Country":"USA, New Zealand, Canada","Awards":"6 wins & 13 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"83%"},{"Source":"Metacritic","Value":"67/100"}],"Metascore":"67","imdbRating":"7.8","imdbVotes":"301,863","imdbID":"tt3896198","Type":"movie","DVD":"22 Aug 2017","BoxOffice":"$389,804,217","Production":"Walt Disney Pictures","Website":"https://marvel.com/guardians","Response":"True"}

    """
    titles = []
    for arg in args:
        for title in arg['data']:
            for f in title.get('folder', {}).get('files'):
                f = f.replace('.', ';;')
                f = f.replace('-', ';;')
                f = f.replace(' ', ';;')
                titles.append(str(f))

    print(titles)
    return titles


@click.command()
@click.option('--home', prompt='Root directory', help='Root directory to scrape for files')
def main(home):

    filetypes = ['.mkv', '.avi', '.mp4']
    fsd = FSDiscovery()
    videos = fsd.discover_rawdata(filetypes, home)
    #series = fsd.filter_series(videos)
    unique_titles(videos)



if __name__ == '__main__':
    main()
