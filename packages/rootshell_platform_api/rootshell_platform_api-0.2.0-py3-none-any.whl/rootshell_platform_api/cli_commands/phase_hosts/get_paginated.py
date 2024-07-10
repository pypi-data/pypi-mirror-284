import click
import json
from rootshell_platform_api.adapters.PhaseHostsAPIClient import PhaseHostsAPIClient

@click.command()
@click.option('--phase_id', required=True, type=str, help='ID of the phase to add the hosts')
@click.option("-l", "--limit", type=int, default=10, help="Pagination limit")
@click.option("-p", "--page", type=int, default=1, help="Pagination page")
@click.option("-s", "--search", type=str, help="Pagination search")
@click.option("-c", "--orderByColumn", default="id", type=str, help="Pagination order by column")
@click.option(
    "-d",
    "--orderByDirection",
    type=click.Choice(["asc", "desc"]),
    help="Pagination order by direction",
    default="desc"
)
def get_paginated(phase_id, limit, page, search, orderbycolumn, orderbydirection):
    api_client = PhaseHostsAPIClient(phase_id)

    try:
        response = api_client.get_entities(
            limit=limit,
            page=page,
            search=search,
            orderByColumn=orderbycolumn,
            orderByDirection=orderbydirection,
        )
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_paginated()
