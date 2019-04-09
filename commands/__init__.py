from .new import *
from .rm import *
from .collab import *
import click

__all__ = [
    'new',
    'rm',
    'collab',
    'cli'
]

@click.group()
def cli():
    pass

cli.add_command(collab)
cli.add_command(new)
cli.add_command(rm)