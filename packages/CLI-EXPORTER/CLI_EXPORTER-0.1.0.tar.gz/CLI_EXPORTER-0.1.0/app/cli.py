import click
from main import extract, menu

@click.group()
def cli():
    pass

cli.add_command(menu)
cli.add_command(extract)

if __name__ == '__main__':
    cli()
