import click
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

@click.command()
def get_paginated():
    api_client = ProjectsAPIClient()

    try:
        response = api_client.get_project_statuses()
        print(json.dumps(response["data"], indent=4))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_paginated()
