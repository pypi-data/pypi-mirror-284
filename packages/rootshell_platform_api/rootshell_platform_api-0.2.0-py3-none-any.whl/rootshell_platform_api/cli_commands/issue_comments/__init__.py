import click
from .create import create
from .get_paginated import get_paginated
from .delete import delete

@click.group(name='issue_comments')
def issue_comments():
    """Commands to manage issue comments."""
    pass

issue_comments.add_command(create)
issue_comments.add_command(get_paginated)
issue_comments.add_command(delete)

__all__ = ['issue_comments']
