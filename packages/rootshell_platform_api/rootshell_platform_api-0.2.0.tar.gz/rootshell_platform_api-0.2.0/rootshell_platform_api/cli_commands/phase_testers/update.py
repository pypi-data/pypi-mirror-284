import click
import json
from rootshell_platform_api.adapters.PhaseTestersAPIClient import PhaseTestersAPIClient

@click.command()
@click.option("--phase_id", required=True, help="The phase we are assigning the user to")
@click.option("--user_id", required=True, help="The user we are assigning to be the phase tester")
def update(phase_id, user_id):
    try:
        response = PhaseTestersAPIClient(phase_id).update_entity(user_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
