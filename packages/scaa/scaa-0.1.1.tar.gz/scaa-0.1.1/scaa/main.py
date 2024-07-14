import click
import requests


@click.command()
@click.argument("path")
def main(path):
    print(path)
    url = "http://35.221.167.116/analyse"
    files = {"file": open(path, "rb")}
    response = requests.post(url, files=files)
    print(response.text)
