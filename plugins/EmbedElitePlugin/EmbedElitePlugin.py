import requests
from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext

def send_request(code, client_id):
    url = f"https://api.embedelite.com/query"
    
    response = requests.get(url)
    
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
        description="Takes the square root of a number",
        name="square_root",
        input_description="The value to take the square root of",
    )
    def square_root(self, number: str) -> str:
        return str(math.sqrt(float(number)))

    @sk_function(
        description="Adds two numbers together",
        name="add",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to add",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to add",
    )
    def VAT_suggestion(self, context: SKContext) -> str:
        return send_request(None, None)