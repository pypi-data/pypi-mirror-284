import click
from .get_paginated import get_paginated
from .update import update
from .delete import delete

@click.group(name='project_tags')
def project_tags():
    """Commands to manage project tags."""
    pass

project_tags.add_command(get_paginated)
project_tags.add_command(update)
project_tags.add_command(delete)

__all__ = ['project_tags']
