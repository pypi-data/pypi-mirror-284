import click
from .get_paginated import get_paginated
from .get_single import get_single

@click.group(name='companies')
def companies():
    """Commands to manage companies."""
    pass

companies.add_command(get_paginated)
companies.add_command(get_single)

__all__ = ['companies']
