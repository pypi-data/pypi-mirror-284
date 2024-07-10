import click
import json
from rootshell_platform_api.adapters.AssetGroupAssetsAPIClient import AssetGroupAssetsAPIClient
from rootshell_platform_api.data_transfer_objects.AssetGroupAssetDTO import AssetGroupAssetDTO

@click.command()
@click.option('--asset_group_id', required=True, type=int, help='Asset Group id to link assets to')
@click.option('--asset_ids', required=True, type=str, multiple=True, help='An array of asset ids')
def update(**kwargs):
    id = kwargs.pop('id')
    dto = AssetGroupAssetDTO(**kwargs)

    try:
        response = AssetGroupAssetsAPIClient().update_entity(id, dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
