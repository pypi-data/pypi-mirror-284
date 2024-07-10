import click
import json
from rootshell_platform_api.adapters.PhaseHostsAPIClient import PhaseHostsAPIClient

@click.command()
@click.option('--phase_id', default=None, type=str, help='ID of the phase')
@click.option('--host_id', default=None, type=str, help='ID of the host')
def get_single(phase_id, host_id):
    api_client = PhaseHostsAPIClient(phase_id)

    try:
        response = api_client.get_entity(enity_id=host_id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
