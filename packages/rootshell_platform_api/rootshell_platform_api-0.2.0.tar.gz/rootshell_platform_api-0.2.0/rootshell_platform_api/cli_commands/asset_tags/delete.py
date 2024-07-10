import click
import json
from rootshell_platform_api.adapters.AssetTagsAPIClient import AssetTagsAPIClient

@click.command()
@click.option('-p', '--asset_id', required=True, help='Asset ID')
@click.option('-t', '--tag_id', required=True, help='Tag ID')
def delete(project_id, tag_id):
    """Delete a tag from an asset."""
    api_client = AssetTagsAPIClient(asset_id)

    try:
        response = api_client.delete_entity(tag_id=tag_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    delete()
