import click
from .get_paginated import get_paginated

@click.group(name='project_statuses')
def project_statuses():
    """Commands to manage project statuses."""
    pass

project_statuses.add_command(get_paginated)

__all__ = ['project_statuses']
