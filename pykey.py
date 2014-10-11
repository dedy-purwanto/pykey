#!/usr/bin/env python
import click

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
