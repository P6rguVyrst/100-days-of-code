# -*- coding: utf-8 -*-

"""Console script for dirmon."""
import time
import logging.config
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import click


@click.command()
@click.option('--path', default='.', help='System path to monitor.')
@click.option('--conf')
def main(path, conf):
    """Console script for dirmon."""

    if not conf:
        raise AssertionError('Missing configuration.')

    logging.config.fileConfig(conf)
    logger = logging.getLogger('dirmon')

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
