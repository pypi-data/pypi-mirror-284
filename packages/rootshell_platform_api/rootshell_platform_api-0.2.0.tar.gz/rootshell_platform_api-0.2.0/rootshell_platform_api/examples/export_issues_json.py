import click
import json
from rootshell_platform_api.adapters.PhaseIssuesAPIClient import PhaseIssuesAPIClient

@click.command()
@click.option('--phase_id', required=True, type=int, help='ID of the phase to retrieve issues for')
@click.option('--output_file', required=True, type=str, help='Output file path to save the issues as JSON')
@click.option("-l", "--limit", type=int, default=10, help="Pagination limit")
@click.option("-s", "--search", type=str, help="Pagination search")
@click.option("-c", "--orderByColumn", default="id", type=str, help="Pagination order by column")
@click.option(
    "-d",
    "--orderByDirection",
    type=click.Choice(["asc", "desc"]),
    help="Pagination order by direction",
    default="desc"
)
def export_issues_to_json(phase_id, output_file, limit, search, orderbycolumn, orderbydirection):
    api_client = PhaseIssuesAPIClient(phase_id)
    all_items = []
    page = 1

    try:
        while True:
            response = api_client.get_entities(
                limit=limit,
                page=page,
                search=search,
                orderByColumn=orderbycolumn,
                orderByDirection=orderbydirection,
            )
            items = response["data"]
            all_items.extend(items)

            if len(items) < limit:
                break

            page += 1

        with open(output_file, 'w') as file:
            json.dump(all_items, file, indent=4)

        click.echo(f"Issues successfully exported to {output_file}")
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    export_issues_to_json()
