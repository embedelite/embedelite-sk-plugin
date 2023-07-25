import requests
import json
import os
from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext

#Change this to your product id
product_id = "vat-rules-eu"

def send_request(query):
    url = "https://api.embedelite.com/query"
    headers = {
        "API-Key": "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",
        "Content-Type": "application/json",
    }
    data = {
        "query": query.result,
        "product_id": product_id,
    }
    #print all keys of query
    print(f"Sending request to {url} with headers {headers} and data {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Received response: {response}")
    if response.status_code == 200:
        # Consider any status other than 2xx an error
        print('Successfully got response from API')
        print(response.text)
    else:
        print('Failed to get response')
        print(f'Status code: {response.status_code}')
        print(response.text)
    return response.text

class EmbedElitePlugin:
    @sk_function(
        description="Receive context from a text embedding product",
        name="semantic_search_query",
    )
    @sk_function_context_parameter(
        name="query",
        description="The query to be answered",
    )
    def semantic_search_query(self, context: SKContext) -> str:
        return send_request(context)