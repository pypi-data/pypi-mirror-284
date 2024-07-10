import click
import json
from rootshell_platform_api.adapters.AssetsAPIClient import AssetsAPIClient
from rootshell_platform_api.data_transfer_objects.AssetDTO import AssetDTO

@click.command()
@click.option('--id', required=True, type=int)
@click.option('--name', default=None, type=str, help='Name of the asset')
@click.option('--hostname', default=None, type=str, help='Hostname of the asset')
@click.option('--ip', type=str, default=None, help='IP address of the asset')
@click.option('--operating_system', type=str, default=None, help='Operating system of the asset')
@click.option('--priority_rating', type=int, default=None, help='Priority rating of the asset')
@click.option('--location', type=str, default=None, help='Location of the asset')
@click.option('--system_owner', type=str, default=None, help='System owner of the asset')
@click.option('--technical_owner', type=str, default=None, help='Technical owner of the asset')
@click.option('--team_system_owner', type=str, default=None, help='Team system owner of the asset')
@click.option('--team_technical_owner', type=str, default=None, help='Team technical owner of the asset')
@click.option('--company_id', default=None, type=int, help='Company ID')
@click.option('--abbreviated_asset_value', type=str, default="", help='Abbreviated asset value')
@click.option('--notes', type=str, default=None, help='Notes about the asset')
@click.option('--tags', type=str, multiple=True, help='Tags for the asset')
def update(**kwargs):
    id = kwargs.pop('id')
    dto = AssetDTO(**kwargs)

    try:
        response = AssetsAPIClient().update_entity(id, dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
