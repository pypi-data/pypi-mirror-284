import click
import json
from rootshell_platform_api.adapters.PhaseHostsAPIClient import PhaseHostsAPIClient
from rootshell_platform_api.data_transfer_objects.PhaseHostDTO import PhaseHostDTO

@click.command()
@click.option('--phase_id', default=None, type=str, help='ID of the phase to add the hosts to')
@click.option('--name', default=None, type=str, help='Name of the host')
@click.option('--ip', type=str, default=None, help='IP address of the host')
@click.option('--hostname', type=str, default=None, help='Hostname of the host')
@click.option('--location', type=str, default=None, help='Operating system of the host')
@click.option('--operating_system', type=str, default=None, help='Operating system of the host')
def create(**kwargs):
    phase_id = kwargs.pop('phase_id')
    dto = PhaseHostDTO(**kwargs)

    try:
        response = PhaseHostsAPIClient(phase_id).create_entity(dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    create()
