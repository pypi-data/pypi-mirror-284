import click
import json
from rootshell_platform_api.adapters.PhaseIssuesAPIClient import PhaseIssuesAPIClient

@click.command()
@click.option('--phase_id', default=None, type=str, help='ID of the phase')
@click.option('--issue_id', default=None, type=str, help='ID of the issue')
def get_single(phase_id, issue_id):
    api_client = PhaseIssuesAPIClient(phase_id)

    try:
        response = api_client.get_entity(enity_id=issue_id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
