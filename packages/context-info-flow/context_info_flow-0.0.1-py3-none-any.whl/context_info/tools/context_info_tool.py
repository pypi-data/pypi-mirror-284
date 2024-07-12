from numbers import Number
from promptflow import tool
import requests
import json


@tool
def get_context_info(
    azure_search_endpoint,
    azure_search_key,
    azure_search_api_version,
    index_name,
    top,
    user_query,
):
    headers = {"Content-Type": "application/json", "api-key": azure_search_key}
    params = {"api-version": azure_search_api_version}

    top = int(top)

    search_payload = {
        "search": f"{user_query}",
        "select": "id,title,chunk,name,location,page_num",
        "top": top,
    }

    resp = requests.post(
        azure_search_endpoint + "/indexes/" + index_name + "/docs/search",
        data=json.dumps(search_payload),
        headers=headers,
        params=params,
    )
    resp.raise_for_status()

    results = resp.json()["value"]
    return results
