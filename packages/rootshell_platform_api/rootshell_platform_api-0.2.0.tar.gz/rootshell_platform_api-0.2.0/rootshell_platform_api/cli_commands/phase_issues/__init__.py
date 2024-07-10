import click
from .get_paginated import get_paginated
from .create import create
from .update import update
from .delete import delete
from .get_single import get_single

@click.group(name='phase_issues')
def phase_issues():
    """Commands to manage phase issues."""
    pass

phase_issues.add_command(get_paginated)
phase_issues.add_command(create)
phase_issues.add_command(update)
phase_issues.add_command(delete)
phase_issues.add_command(get_single)

__all__ = ['phase_issues']
