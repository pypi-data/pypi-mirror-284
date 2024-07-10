import click
import json
from rootshell_platform_api.adapters.IssueCommentsAPIClient import IssueCommentsAPIClient

@click.command()
@click.option("--phase_id", required=True, help="Phase ID")
@click.option("--issue_id", required=True, help="Issue ID")
@click.option("-l", "--limit", type=int, default=10, help="Pagination limit")
@click.option("-p", "--page", type=int, default=1, help="Pagination page")
@click.option("-s", "--search", type=str, help="Pagination search")
@click.option("-c", "--orderByColumn", default="name", type=str, help="Pagination order by column")
@click.option(
    "-d",
    "--orderByDirection",
    type=click.Choice(["asc", "desc"]),
    help="Pagination order by direction",
    default="asc"
)
def get_paginated(phase_id, issue_id, limit, page, search, orderbycolumn, orderbydirection):
    api_client = IssueCommentsAPIClient(phase_id, issue_id)

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
