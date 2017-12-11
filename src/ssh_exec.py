#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import click
import paramiko
import logging
from subprocess import call
import pygame
import time

LOGGER = logging.getLogger(__name__)

@click.command()
@click.option('--host', help='Remote host IP.')
@click.option('--port', default=22, help='Remote host PORT.')
@click.option('--user', help='Username to connect with.')
@click.option('--command', help='Remote host IP.')
def event_listener(host, port, user, command):

    ssh = paramiko.SSHClient()
    ssh_config = paramiko.SSHConfig()
    user_config_file = os.path.expanduser("~/.ssh/config")

    if os.path.exists(user_config_file):
        with open(user_config_file) as f:
            ssh_config.parse(f)

    cfg = {'hostname': host, 'username': user}
    user_config = ssh_config.lookup(cfg['hostname'])

    for k in ('hostname', 'username', 'port'):
        if k in user_config:
            cfg[k] = user_config[k]

    if 'proxycommand' in user_config:
        cfg['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(**cfg)

    LOGGER.info("Executing {}".format(command))
    stdin , stdout, stderr = ssh.exec_command(command, get_pty=True)

    for line in iter(stdout.readline, ""):
        # DO something with event stream
        print(line, end="")

    ssh.close()

    pygame.mixer.init()
    pygame.mixer.music.load('02-Zvezda po imeni solnce.mp3')
    pygame.mixer.music.play()
    time.sleep(300)


if __name__ == '__main__':
    event_listener()
