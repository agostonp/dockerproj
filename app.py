#!/usr/bin!env python
import click

@click.command()
def hello():
    click.echo('Hello World!')
    click.echo('Whats up Doc?')
    
if __name__ == '__main__':
    hello()
    