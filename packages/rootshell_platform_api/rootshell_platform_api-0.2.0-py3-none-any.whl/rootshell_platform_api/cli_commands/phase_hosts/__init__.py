import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='phase_hosts')
def phase_hosts():
    """Commands to manage phase hosts."""
    pass

phase_hosts.add_command(get_paginated)
phase_hosts.add_command(create)
phase_hosts.add_command(update)
phase_hosts.add_command(delete)
phase_hosts.add_command(get_single)

__all__ = ['phase_hosts']
