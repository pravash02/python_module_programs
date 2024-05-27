import dlt
from dlt.sources.helpers import requests

url = "https://api.github.com/repos/dlt-hub/dlt/issues"


def get_response():
    # Make a request and check if it was successful
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())
    return response.json()


if __name__ == '__main__':
    # configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name="github_issues",
        destination="duckdb",
        dataset_name="data",
    )

    # The response contains a list of issues
    load_info = pipeline.run(get_response(), table_name="test")

    print(load_info)
