import click
import json
from rootshell_platform_api.adapters.PhasesAPIClient import PhasesAPIClient
from rootshell_platform_api.data_transfer_objects.PhaseDTO import PhaseDTO

@click.command()
@click.option('--id', required=True, type=int)
@click.option('--project_id', required=True, type=int)
@click.option('--name', required=True, type=str)
@click.option('--status', required=True, type=int)
@click.option('--executive_summary', required=True, type=str)
@click.option('--caveat', type=str, required=True)
@click.option('--scope_summary', required=True, type=str)
@click.option('--assessment_context', required=True, type=str)
@click.option('--start_date', type=str, default=None)
@click.option('--end_date', type=str, default=None)
@click.option('--location', type=str, default=None)
@click.option('--tester_id', type=int, default=None)
@click.option('--test_type_id', type=int, default=None)
@click.option('--approved_at', type=str, default=None)
@click.option('--approved_by', type=int, default=None)
@click.option('--completed_by', type=int, default=None)
@click.option('--probability', type=int, default=None)
@click.option('--questionnaire_id', type=int, default=None)
def update(**kwargs):
    id = kwargs.pop('id')
    dto = PhaseDTO(**kwargs)

    try:
        response = PhasesAPIClient().update_entity(id, dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
