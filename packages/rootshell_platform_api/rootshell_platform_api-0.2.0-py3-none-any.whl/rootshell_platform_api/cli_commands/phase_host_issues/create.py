import click
import json
from rootshell_platform_api.adapters.PhaseHostIssuesAPIClient import PhaseHostIssuesAPIClient
from rootshell_platform_api.data_transfer_objects.PhaseHostIssueDTO import PhaseHostIssueDTO

@click.command()
@click.option('--phase_id', required=True, type=str, help='Phase ID')
@click.option('--issue_id', required=True, type=str, help='Issue ID that we want to link to the host')
@click.option('--host_id', required=True, type=str, help='Host ID that we want to link to the issue')
@click.option('--port', default=None, type=str, help='The port of the host')
@click.option('--protocol', type=str, default=None, help='The protocol of the host')
@click.option('--service', type=str, default=None, help='The service of the host')
def create(**kwargs):
    dto = PhaseHostIssueDTO(**kwargs)

    try:
        response = PhaseHostIssuesAPIClient(phase_id, issue_id).create_entity(dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    create()
