import click
import json
from rootshell_platform_api.adapters.PhaseHostIssuesAPIClient import PhaseHostIssuesAPIClient

@click.command()
@click.option('--phase_id', required=True, type=str, help='Phase ID')
@click.option('--issue_id', required=True, type=str, help='Issue ID that we want to link to the host')
@click.option('--host_issue_id', default=None, type=str, help='Host Issue ID that we want to update')
def get_single(id):
    api_client = AssetsAPIClient(phase_id, issue_id)

    try:
        response = api_client.get_entity(entity_id=host_issue_id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
