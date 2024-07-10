import click
from .get_paginated import get_paginated

@click.group(name='test_types')
def test_types():
    """Commands to manage test types."""
    pass

test_types.add_command(get_paginated)

__all__ = ['test_types']
