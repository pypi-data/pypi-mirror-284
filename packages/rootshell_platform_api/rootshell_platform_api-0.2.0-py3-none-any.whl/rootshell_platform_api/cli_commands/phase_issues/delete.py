import click
import json
from rootshell_platform_api.adapters.PhaseIssuesAPIClient import PhaseIssuesAPIClient

@click.command()
@click.option('--phase_id', default=None, type=str, help='ID of the phase')
@click.option('--issue_id', default=None, type=str, help='ID of the issue')
def delete(phase_id, issue_id):
    try:
        response = PhaseIssuesAPIClient(phase_id).delete_entity(issue_id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
