import click
import json
from rootshell_platform_api.adapters.MergeSettingsAPIClient import MergeSettingsAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the setting")
def get_single(id):
    api_client = MergeSettingsAPIClient()

    try:
        response = api_client.get_entity(entity_id=id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
