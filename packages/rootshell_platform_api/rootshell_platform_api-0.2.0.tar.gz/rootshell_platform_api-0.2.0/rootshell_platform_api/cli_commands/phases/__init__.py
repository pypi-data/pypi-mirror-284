import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='phases')
def phases():
    """Commands to manage phases."""
    pass

phases.add_command(get_paginated)
phases.add_command(create)
phases.add_command(update)
phases.add_command(delete)
phases.add_command(get_single)

__all__ = ['phases']
