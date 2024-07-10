import click
import json
from rootshell_platform_api.adapters.PhaseHostsAPIClient import PhaseHostsAPIClient

@click.command()
@click.option('--phase_id', default=None, type=str, help='ID of the phase')
@click.option('--host_id', default=None, type=str, help='ID of the host')
def delete(phase_id, host_id):
    try:
        response = PhaseHostsAPIClient(phase_id).delete_entity(host_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
