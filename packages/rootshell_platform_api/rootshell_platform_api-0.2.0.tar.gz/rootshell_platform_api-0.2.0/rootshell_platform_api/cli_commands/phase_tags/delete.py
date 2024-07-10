import click
import json
from rootshell_platform_api.adapters.PhaseTagsAPIClient import PhaseTagsAPIClient

@click.command()
@click.option('-p', '--phase_id', required=True, help='Asset ID')
@click.option('-t', '--tag_id', required=True, help='Tag ID')
def delete(project_id, tag_id):
    """Delete a tag from a phase."""
    api_client = PhaseTagsAPIClient(phase_id)

    try:
        response = api_client.delete_entity(tag_id=tag_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    delete()
