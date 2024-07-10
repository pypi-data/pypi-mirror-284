import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='assets')
def assets():
    """Commands to manage assets."""
    pass

assets.add_command(get_paginated)
assets.add_command(create)
assets.add_command(update)
assets.add_command(delete)
assets.add_command(get_single)

__all__ = ['assets']
