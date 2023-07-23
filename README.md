# SK Hackathon EmbedElite Plugin

This project is creating a plugin for the EmbedElite marketplace for the SK Hackathon. The plugin facilitates fetching ready-made premium embeddings via an API.

# Building Native Functions

This console application provides a finished solution for the [Building native functions](https://learn.microsoft.com/en-us/semantic-kernel/ai-orchestration/native-functions) document.

## Requirements

- [Python](https://www.python.org/downloads/) 3.8 or higher
  - [Poetry](https://python-poetry.org/) for package handling and dependency management
  - [Semantic Kernel Tools](https://marketplace.visualstudio.com/items?itemName=ms-semantic-kernel.semantic-kernel)

## Sample Configuration

A `.env` file housed within the project is used for configuring the sample. It contains API keys and other confidential settings.

Ensure you possess an
[Open AI API Key](https://openai.com/api/) or an
[Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)

Create a new file titled `.env` by duplicating the `.env.example` file. Then transfer your API keys into the new `.env` file:

```
OPENAI_API_KEY=""
OPENAI_ORG_ID=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
```

## Sample Execution

Within Visual Studio Code, press `F5` to run the console application. As defined in `launch.json` and `tasks.json`, Visual Studio Code will implement `poetry install` and then `python hello_world/main.py`

To build and execute the console application from the terminal, apply the following commands:

```powershell
poetry install
poetry run python main.py
```