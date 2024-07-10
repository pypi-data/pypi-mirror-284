import click
from .update import update
from .get_paginated import get_paginated
from .delete import delete

@click.group(name='phase_testers')
def phase_testers():
    """Commands to manage phase testers."""
    pass

phase_testers.add_command(update)
phase_testers.add_command(get_paginated)
phase_testers.add_command(delete)

__all__ = ['phase_testers']
