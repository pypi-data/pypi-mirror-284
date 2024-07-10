import click
import json
from rootshell_platform_api.adapters.AssetsAPIClient import AssetsAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the asset to be deleted")
def delete(id):
    try:
        response = AssetsAPIClient().delete_entity(id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
