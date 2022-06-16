import click


@click.group()
def db():
    pass


@click.group()
def modify():
    pass


@modify.command()
@click.argument("name")
def create(name):
    click.echo(name)


@modify.command()
@click.option("--rename", "-rn", "rename", help="Give a new name if you want to rename the DB")
@click.argument("name")
def alter(rename, name):
    click.echo(rename)
    click.echo(name)


@click.command()
@click.option("--force/--no-force", "-f/-nf", "force", default=False, type=bool, help="Forced deletion, default = False")
@click.argument("name")
def drop(force, name):
    click.echo(force)
    click.echo(name)


db.add_command(modify)
db.add_command(drop)

if __name__ == '__main__':
    db()
