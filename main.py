import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    OpenAITextCompletion,
    AzureTextCompletion,
)
from plugins.EmbedElitePlugin.EmbedElitePlugin import EmbedElitePlugin

async def main():
    # Initialize the kernel
    kernel = sk.Kernel()

    # Configure AI service used by the kernel. Load settings from the .env file.
    useAzureOpenAI = False
    if useAzureOpenAI:
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", AzureTextCompletion(deployment, endpoint, api_key)
        )
    else:
        api_key, org_id = sk.openai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
        )

    pluginsDirectory = "./plugins"

    # Import the semantic functions
    kernel.import_semantic_skill_from_directory(pluginsDirectory, "EmbedElitePlugin")

    # Import the EmbedElite Plugin
    embedElitePlugin = kernel.import_skill(
        EmbedElitePlugin(), "EmbedElitePlugin"
    )

    # Call EmbedElitePlugin to fetch embeddings
    embeddings = await embedElitePlugin["get_embeddings"].invoke_async(
        "Some text to embed."
    )
    print(embeddings["output"])


# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
