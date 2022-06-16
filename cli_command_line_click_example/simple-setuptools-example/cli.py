import click


@click.command()
@click.argument("name")
def cli(name):
    """Simple cli utility using python click"""
    click.echo(f"name = {name}")


if __name__ == '__main__':
    cli()
