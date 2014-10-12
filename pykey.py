#!/usr/bin/env python
import os
import ConfigParser

import click

USER_PATH = os.path.expanduser('~')
CONFIG_FILENAME = os.path.join(USER_PATH, '.pykeyrc')
DEFAULT_STORAGE_PATH = os.path.join(USER_PATH, '.pykey')

def get_config():
    config = ConfigParser.RawConfigParser()
    if os.path.isfile(CONFIG_FILENAME):
        configfile = open(CONFIG_FILENAME, 'r')
        config.readfp(configfile)
        configfile.close()

    return config

def write_config(config):
    configfile = open(CONFIG_FILENAME, 'w')
    config.write(configfile)
    return config

@click.group()
def main():
    pass

@main.command()
def new():
    pass

@main.command()
@click.argument('id')
def edit(id):
    pass

@main.command()
@click.argument('id')
def get(id):
    pass

@main.command()
@click.argument('keyword')
def find(keyword):
    pass

@main.group()
def vaults():
    pass

@vaults.command()
def new():
    pass

@vaults.command()
@click.argument('id')
def edit(id):
    pass

if __name__ == '__main__':
    main()
