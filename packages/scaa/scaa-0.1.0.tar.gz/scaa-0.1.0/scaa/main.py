import click
import requests


@click.command()
@click.argument("path")
def main(path):
    print(path)
