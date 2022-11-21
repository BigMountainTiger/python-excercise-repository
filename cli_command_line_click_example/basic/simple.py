import click


@click.command()
@click.option("--int", "-i", "a_int", required=True, type=int, help="An integer")
@click.option("--optional", "-op", "a_optional", required=False, help="This is an optional text parameter")
@click.option("--string", "-s", "a_string", default="Song", type=str, help="A text string")
@click.option('--array', '-a', "a_array", required=False, multiple=True,
              help="This is an array variable, you can pass more than 1 values")
@click.argument("name")
def simple(a_int, a_optional, a_string, a_array, name):
    """Simple cli utility using python click"""

    click.echo(a_int)
    click.echo(a_optional or "None")
    click.echo(a_string)
    click.echo(a_array)

    click.echo(name)


if __name__ == '__main__':
    simple()
