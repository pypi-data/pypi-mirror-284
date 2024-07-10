import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='asset_groups')
def asset_groups():
    """Commands to manage asset groups."""
    pass

asset_groups.add_command(get_paginated)
asset_groups.add_command(create)
asset_groups.add_command(update)
asset_groups.add_command(delete)
asset_groups.add_command(get_single)

__all__ = ['asset_groups']
