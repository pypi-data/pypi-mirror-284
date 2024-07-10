import click
from .get_paginated import get_paginated
from .update import update

@click.group(name='asset_group_assets')
def asset_group_assets():
    """Commands to manage asset group assets."""
    pass

asset_group_assets.add_command(get_paginated)
asset_group_assets.add_command(update)

__all__ = ['asset_group_assets']
