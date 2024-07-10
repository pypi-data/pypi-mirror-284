import click
import json
from rootshell_platform_api.adapters.ProjectTagsAPIClient import ProjectTagsAPIClient

@click.command()
@click.option('-p', '--project_id', required=True, help='Project ID')
@click.option('-t', '--tag_id', required=True, help='Tag ID')
def update(project_id, tag_id):
    """Update a tag for a project."""
    api_client = ProjectTagsAPIClient(project_id)

    try:
        response = api_client.update_project_tag(tag_id=tag_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    update()
