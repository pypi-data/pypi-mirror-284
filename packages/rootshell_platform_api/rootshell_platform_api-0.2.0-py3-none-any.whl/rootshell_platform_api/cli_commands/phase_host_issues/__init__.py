import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='phase_host_issues')
def phase_host_issues():
    """Commands to manage phase hosts issues."""
    pass

phase_host_issues.add_command(get_paginated)
phase_host_issues.add_command(create)
phase_host_issues.add_command(update)
phase_host_issues.add_command(delete)
phase_host_issues.add_command(get_single)

__all__ = ['phase_host_issues']
