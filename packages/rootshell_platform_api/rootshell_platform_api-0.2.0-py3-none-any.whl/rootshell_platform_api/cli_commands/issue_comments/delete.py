import click
import json
from rootshell_platform_api.adapters.IssueCommentsAPIClient import IssueCommentsAPIClient

@click.command()
@click.option("--phase_id", required=True, help="Phase ID")
@click.option("--issue_id", required=True, help="Issue ID")
@click.option("--comment_id", required=True, help="Comment ID")
def delete(id, name):
    try:
        response = IssueCommentsAPIClient(phase_id, issue_id).delete_entity(id, name)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
