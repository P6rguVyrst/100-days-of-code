#!/usr/bin/env python3
# -*- coding: utf8 -*-
import logging
import redis
import time

LOGGER = logging.getLogger(__name__)


def consumer():
    r = redis.Redis()
    while True:
        val = r.blpop('queue')
        print('Consuming: (%s, %s)' % val)


if __name__ == '__main__':
    LOGGER.info("Starting consumer: ")
    consumer()
