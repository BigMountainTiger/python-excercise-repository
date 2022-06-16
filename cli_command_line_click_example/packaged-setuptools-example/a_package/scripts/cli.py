import click

from ..utils import say_something

@click.command()
@click.argument("name")
def cli(name):
    """Simple cli utility using python click"""
    click.echo(f"name = {name}")

    click.echo(say_something())


if __name__ == '__main__':
    cli()
