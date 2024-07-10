import click
from .get_paginated import get_paginated
from .update import update
from .delete import delete

@click.group(name='phase_tags')
def phase_tags():
    """Commands to manage phase tags."""
    pass

phase_tags.add_command(get_paginated)
phase_tags.add_command(update)
phase_tags.add_command(delete)

__all__ = ['phase_tags']
