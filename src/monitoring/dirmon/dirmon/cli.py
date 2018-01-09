# -*- coding: utf-8 -*-

"""Console script for dirmon."""
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import click


@click.command()
@click.option('--path', default='.', help='System path to monitor.')
def main(path):
    """Console script for dirmon."""
    #TODO: Proper logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
