# -*- coding: utf-8 -*-
import logging
from pprint import pprint as pp
import json
import click

from project.filesystem import FSDiscovery
from project.media import Media


def send_data(data):
    pp(data)
    uri = 'http://127.0.0.1:5000/notify'
    extra = {'msg_type': 'media'}
    d = {**data, **extra}
    #r = requests.post(uri, data=json.dumps(d))
    #print(json.dumps(d))


@click.command()
@click.option('--home', default='.', help='Root directory to scrape for files')
@click.option('--filetypes', '-f', help='Comma separated list of diletypes')
@click.option('--loglevel', '-l', default=4, help='Specify loglevel')
@click.option('--config', '-c')
def main(home, filetypes, loglevel):

    logger = logging.getLogger(__name__)
    #logger.setLevel(6)
    if not filetypes:
        raise SystemExit('Please specify filetypes')

    filetypes = filetypes.split(',')
    logger.debug('Searching for following filetypes: %s', filetypes)

    fsd = FSDiscovery()
    data = fsd.discover_rawdata(filetypes, home)
    logger.warning('Found following data: %s', data)

    media = Media()
    movies = media.unique_titles(data, 'movies')
    series = media.unique_titles(data, 'series')
    uniq_movies = list(set(movies['titles']))
    uniq_series = list(set(series['titles']))

    payload = {
        'movies': uniq_movies,
        'series': uniq_series,
    }
    send_data(payload)


if __name__ == '__main__':
    main()
