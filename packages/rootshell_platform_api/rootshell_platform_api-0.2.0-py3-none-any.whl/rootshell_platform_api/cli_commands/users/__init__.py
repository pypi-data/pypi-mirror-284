import click
from .get_paginated import get_paginated

@click.group(name='users')
def users():
    """Commands to manage users."""
    pass

users.add_command(get_paginated)

__all__ = ['users']
