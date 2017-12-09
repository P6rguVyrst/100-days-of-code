#!/usr/bin/env python3
# -*- coding: utf8 -*-
import logging
import redis
import time

LOGGER = logging.getLogger(__name__)


def producer():
    r = redis.Redis()
    i = 0
    while True:
        r.rpush('queue', 'Message %d' % i)
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    LOGGER.info("Starting producer: ")
    producer()
