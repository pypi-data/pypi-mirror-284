import click
from .get_paginated import get_paginated

@click.group(name='issues')
def issues():
    """Commands to manage issues."""
    pass

issues.add_command(get_paginated)

__all__ = ['issues']
