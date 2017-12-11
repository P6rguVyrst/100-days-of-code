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


@click.command()
@click.option('--home', prompt='Root directory', help='Root directory to scrape for files')
def main(home):

    filetypes = ['.mkv', '.avi', '.mp4']

    fsd = FSDiscovery()
    videos = fsd.discover_rawdata(filetypes, home)
    series = fsd.filter_series(videos)
    print(json.dumps(dict(data=series)))

if __name__ == '__main__':
    main()
