import click
from .get_paginated import get_paginated
from .update import update
from .delete import delete

@click.group(name='asset_tags')
def asset_tags():
    """Commands to manage asset tags."""
    pass

asset_tags.add_command(get_paginated)
asset_tags.add_command(update)
asset_tags.add_command(delete)

__all__ = ['asset_tags']
