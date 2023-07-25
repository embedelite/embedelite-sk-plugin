import requests
import json
import os
from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext

def send_request(collection_name, query):
    url = "https://api.embedelite.com/query"
    headers = {
        "API-Key": os.getenv("EMBEDELITE_API_KEY"),
        "Content-Type": "application/json",
    }
    data = {
        "query": query,
        "collection_name": collection_name,
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        # Consider any status other than 2xx an error
        print('Successfully got response from API')
        print(response.text)
    else:
        print('Failed to get response')
        print(f'Status code: {response.status_code}')
        print(response.text)

class EmbedElitePlugin:
    @sk_function(
        description="Receive context from an text embedding",
        name="semantic_search_query",
    )
    @sk_function_context_parameter(
        name="collection_name",
        description="Name of the collection to query",
    )
    @sk_function_context_parameter(
        name="query",
        description="The query for the embedding",
    )
    def semantic_search_query(self, context: SKContext) -> str:
        return send_request(context.get("collection_name"), context.get("query"))
