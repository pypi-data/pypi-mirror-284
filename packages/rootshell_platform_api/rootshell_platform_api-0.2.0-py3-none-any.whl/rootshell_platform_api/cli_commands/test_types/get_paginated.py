import click
import json
from rootshell_platform_api.adapters.TestTypesAPIClient import TestTypesAPIClient

@click.command()
@click.option('-l', '--limit', type=int, default=10, help='Pagination limit')
@click.option('-p', '--page', type=int, default=1, help='Pagination page')
@click.option('-s', '--search', type=str, help='Pagination search')
@click.option('-c', '--order-by-column', type=str, help='Pagination order by column')
@click.option('-d', '--order-by-direction', help='Pagination order by direction', type=click.Choice(['asc', 'desc'], case_sensitive=False))
def get_paginated(limit, page, search, order_by_column, order_by_direction):
    api_client = TestTypesAPIClient()

    try:
        response = api_client.get_test_types(
            limit=limit,
            page=page,
            search=search,
            orderByColumn=order_by_column,
            orderByDirection=order_by_direction,
        )
        print(json.dumps(response["data"], indent=4))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_paginated()
