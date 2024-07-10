import click
from .get_paginated import get_paginated
from .get_single import get_single

@click.group(name='merge_settings')
def merge_settings():
    """Commands to manage merge settings."""
    pass

merge_settings.add_command(get_paginated)
merge_settings.add_command(get_single)

__all__ = ['merge_settings']
