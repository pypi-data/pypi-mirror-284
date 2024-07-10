import click
import json
from rootshell_platform_api.adapters.PhaseTagsAPIClient import PhaseTagsAPIClient

@click.command()
@click.option('--id', required=True, type=int, help='Project ID')
@click.option('-l', '--limit', type=int, default=10, help='Pagination limit')
@click.option('-p', '--page', type=int, default=1, help='Pagination page')
def get_paginated(id, limit, page):
    api_client = PhaseTagsAPIClient(id)

    try:
        response = api_client.get_entities(limit=limit, page=page)
        print(json.dumps(response["data"], indent=4))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_paginated()
