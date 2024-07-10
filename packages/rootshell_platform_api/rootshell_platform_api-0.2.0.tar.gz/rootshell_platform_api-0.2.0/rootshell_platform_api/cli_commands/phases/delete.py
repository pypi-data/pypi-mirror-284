import click
import json
from rootshell_platform_api.adapters.PhasesAPIClient import PhasesAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the phase to be deleted")
def delete(id):
    try:
        response = PhasesAPIClient().delete_entity(id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
