import click
from .get_paginated import get_paginated

@click.group(name='project_service_types')
def project_service_types():
    """Commands to manage project service types."""
    pass

project_service_types.add_command(get_paginated)

__all__ = ['project_service_types']
