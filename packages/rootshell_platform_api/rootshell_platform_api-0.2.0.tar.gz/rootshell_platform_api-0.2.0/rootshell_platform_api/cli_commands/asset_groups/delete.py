import click
import json
from rootshell_platform_api.adapters.AssetGroupsAPIClient import AssetGroupsAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the asset group to be deleted")
def delete(id):
    try:
        response = AssetGroupsAPIClient().delete_entity(id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
