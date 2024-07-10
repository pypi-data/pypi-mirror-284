import click
import json
from rootshell_platform_api.adapters.AssetGroupsAPIClient import AssetGroupsAPIClient
from rootshell_platform_api.data_transfer_objects.AssetGroupDTO import AssetGroupDTO

@click.command()
@click.option('--id', required=True, type=int)
@click.option('--name', required=True, type=str, help='Name of the asset group')
@click.option('--merge_setting_id', required=True, type=str, help='Merge Setting ID of the asset group')
@click.option('--description', type=str, required=True, help='Description of the asset group')
def update(**kwargs):
    id = kwargs.pop('id')
    dto = AssetGroupDTO(**kwargs)

    try:
        response = AssetGroupsAPIClient().update_entity(id, dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
