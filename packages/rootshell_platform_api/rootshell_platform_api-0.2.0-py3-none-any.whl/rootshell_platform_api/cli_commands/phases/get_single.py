import click
import json
from rootshell_platform_api.adapters.PhasesAPIClient import PhasesAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the phase")
def get_single(id):
    api_client = PhasesAPIClient()

    try:
        response = api_client.get_entity(entity_id=id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
