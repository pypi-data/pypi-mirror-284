import click
import json
from rootshell_platform_api.adapters.PhaseTagsAPIClient import PhaseTagsAPIClient

@click.command()
@click.option('-p', '--phase_id', required=True, help='Asset ID')
@click.option('-t', '--tag_id', required=True, help='Tag ID')
def update(phase_id, tag_id):
    """Update a tag for a phase."""
    api_client = PhaseTagsAPIClient(project_id)

    try:
        response = api_client.update_entity(tag_id=tag_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    update()
