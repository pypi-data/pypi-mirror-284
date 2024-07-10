import click
from .get_paginated import get_paginated

@click.group(name='project_remediation_types')
def project_remediation_types():
    """Commands to manage project remediation types."""
    pass

project_remediation_types.add_command(get_paginated)

__all__ = ['project_remediation_types']
