import click
import importlib

@click.group()
def cli():
    pass

entity_groups = [
    'assets',
    'asset_groups',
    'asset_group_assets',
    'asset_tags',
    'companies',
    'tags',
    'projects',
    'users',
    'test_types',
    'issues',
    'issue_comments',
    'merge_settings',
    'phases',
    'phase_hosts',
    'phase_host_issues',
    'phase_tags',
    'phase_issues',
    'phase_testers',
    'project_statuses',
    'project_tags',
    'project_service_types',
    'project_remediation_types',
]

for entity in entity_groups:
    try:
        module = importlib.import_module(f'rootshell_platform_api.cli_commands.{entity}')
        if hasattr(module, '__all__'):
            for command_name in module.__all__:
                command = getattr(module, command_name)
                cli.add_command(command)
        else:
            click.echo(f"Module '{entity}' does not define __all__.")

    except AttributeError as e:
        click.echo(f"Failed to load commands for '{entity}': {e}")
    except ModuleNotFoundError as e:
        click.echo(f"Module '{entity}' not found: {e}")

if __name__ == '__main__':
    cli()
