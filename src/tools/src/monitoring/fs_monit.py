import sys
import time
import logging
import logging.config
from watchdog.observers import Observer
from watchdog.events import (
    LoggingEventHandler,
    FileSystemEventHandler,
)

import redis
import click

# TODO: refine and package it
# Direct filesystem events to /dev/jsonlog
logging.config.fileConfig('fsmonitor.cfg')
LOGGER = logging.getLogger('fsmonitor')


class RedisHandler(FileSystemEventHandler):
    """Direct filesystem events to redis."""

    def __init__(self, observer):
        self.observer = observer
        self.redis = redis.Redis()
    def on_created(self, event):
        self.rpush('queue', event)
        print(event)
    def on_moved(self, event):
        self.rpush('queue', event)
        print(event)
    def on_deleted(self, event):
        self.rpush('queue', event)
        print(event)
    def on_modified(self, event):
        self.rpush('queue', event)
        print(event)



@click.command()
@click.option('--directory', default=None, help='Directory to monitor.')
def monitor(directory):
    path = directory if directory else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    #event_handler = RedisHandler(observer)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()





if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO,
    #                    format='%(asctime)s - %(message)s',
    #                    datefmt='%Y-%m-%d %H:%M:%S')
        monitor()
