import click
import json
from datetime import datetime
from rootshell_platform_api.adapters.PhaseIssuesAPIClient import PhaseIssuesAPIClient
from rootshell_platform_api.data_transfer_objects.PhaseIssueDTO import PhaseIssueDTO

@click.command()
@click.option('--phase_id', required=True, type=int, help='ID of the phase to add the issue to')
@click.option('--issue_id', required=True, type=int, help='ID of the issue')
@click.option('--name', required=True, type=str, help='Name of the issue')
@click.option('--cvss_vector', required=True, type=str, help='CVSS vector of the issue')
@click.option('--cvss_base_score', required=True, type=float, help='CVSS base score of the issue')
@click.option('--cvss_temporal_score', required=True, type=float, help='CVSS temporal score of the issue')
@click.option('--cvss_environmental_score', required=True, type=float, help='CVSS environmental score of the issue')
@click.option('--risk_rating', required=True, type=int, help='Risk rating of the issue')
@click.option('--finding', required=True, type=str, help='Finding of the issue')
@click.option('--references', required=True, type=str, help='References for the issue')
@click.option('--summary', required=True, type=str, help='Summary of the issue')
@click.option('--technical_details', required=True, type=str, help='Technical details of the issue')
@click.option('--recommendation', required=True, type=str, help='Recommendation for the issue')
@click.option('--status', required=True, type=int, help='Status of the issue')
@click.option('--confirmed_at', required=False, type=str, help='Confirmed at date of the issue (ISO format)')
@click.option('--published_at', required=False, type=str, help='Published at date of the issue (ISO format)')
@click.option('--exploit_available', required=True, type=bool, help='Exploit available for the issue')
@click.option('--active_exploit', required=True, type=int, help='Active exploit status of the issue')
@click.option('--hosts', default="[]", type=str, help='Hosts affected by the issue (JSON format)')
def update(**kwargs):
    phase_id = kwargs.pop('phase_id')
    issue_id = kwargs.pop('issue_id')

    hosts = kwargs.get('hosts')
    if hosts:
        kwargs['hosts'] = json.loads(hosts)

    if 'confirmed_at' in kwargs and kwargs['confirmed_at']:
        kwargs['confirmed_at'] = datetime.fromisoformat(kwargs['confirmed_at'])
    if 'published_at' in kwargs and kwargs['published_at']:
        kwargs['published_at'] = datetime.fromisoformat(kwargs['published_at'])

    dto = PhaseIssueDTO(**kwargs)

    try:
        response = PhaseIssuesAPIClient(phase_id).update_entity(issue_id, dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
