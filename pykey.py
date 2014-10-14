#!/usr/bin/env python
import os
import ConfigParser
import binascii

import click
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES

USER_PATH = os.path.expanduser('~')
CONFIG_FILENAME = os.path.join(USER_PATH, '.pykeyrc')
DEFAULT_STORAGE_PATH = os.path.join(USER_PATH, '.pykey')
DEFAULT_SECTION = 'main'
PASSPHRASE_DEFAULT_ITERATIONS = 50000
AES_DEFAULT_DEPTH = 16

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

def config_has_default(config):
    config = get_config()
    return config.has_section(DEFAULT_SECTION)

def create_vault(passphrase):
    salt = os.urandom(AES_DEFAULT_DEPTH)
    iv = os.urandom(AES_DEFAULT_DEPTH)
    key = PBKDF2(
            passphrase, 
            salt, 
            dkLen=16, 
            count=PASSPHRASE_DEFAULT_ITERATIONS)

    return dict(
            cipher='AES-%s' % AES_DEFAULT_DEPTH,
            key=key.encode('hex'), 
            salt=salt.encode('hex'), 
            iv=iv.encode('hex'), 
            iterations=PASSPHRASE_DEFAULT_ITERATIONS)

def save_vault(vault, name, key_filename=None, vault_filename=None):
    if not key_filename:
        key_filename = os.path.join(DEFAULT_STORAGE_PATH, "%s.key" % name)

    if not vault_filename:
        vault_filename = os.path.join(DEFAULT_STORAGE_PATH, "%s.json" % name)

    config = ConfigParser.RawConfigParser()
    config.add_section('cipher')
    config.set('cipher', 'cipher', vault['cipher'])
    config.set('cipher', 'salt', vault['salt'])
    config.set('cipher', 'iv', vault['iv'])
    config.set('cipher', 'iterations', vault['iterations'])
    with open(key_filename, 'w') as f:
        config.write(f)

    return dict(
            key_filename=key_filename, 
            vault_filename=vault_filename, 
            name=name)


def register_vault(saved_vault):
    config = get_config()
    name = saved_vault['name']
    if not config.has_section(name):
        config.add_section(name)

    config.set(name, 'vault', saved_vault['vault_filename'])
    config.set(name, 'key', saved_vault['key_filename'])
    write_config(config)


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
