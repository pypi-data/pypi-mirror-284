import click
import json
from rootshell_platform_api.adapters.IssueCommentsAPIClient import IssueCommentsAPIClient
from rootshell_platform_api.data_transfer_objects.IssueCommentDTO import IssueCommentDTO

@click.command()
@click.option("--phase_id", required=True, help="Phase ID")
@click.option("--issue_id", required=True, type=int, help="Issue ID")
@click.option("--comment", required=True, type=str, help="Comment")
def create(**kwargs):
    dto = IssueCommentDTO(**kwargs)

    try:
        response = IssueCommentsAPIClient(phase_id, issue_id).create_entity(dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    create()
