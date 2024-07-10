import click
import json
from rootshell_platform_api.adapters.PhaseHostIssuesAPIClient import PhaseHostIssuesAPIClient

@click.command()
@click.option('--phase_id', required=True, type=str, help='Phase ID')
@click.option('--issue_id', required=True, type=str, help='Issue ID that we want to link to the host')
@click.option('--host_issue_id', required=True, type=str, help='Host Issue ID that we want to update')
def delete(id):
    try:
        response = PhaseHostIssuesAPIClient(phase_id, issue_id).delete_entity(host_issue_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
