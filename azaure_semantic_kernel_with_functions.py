from dotenv import load_dotenv
import os
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
import asyncio


async def main():
    load_dotenv()
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    api_key = os.environ["AZURE_OPENAI_API_KEY"]

    kernel = Kernel()
    kernel.add_service(AzureChatCompletion(
            deployment_name=deployment_name,
            endpoint=endpoint,
            api_key=api_key,
        ))

    script_directory = os.path.dirname(__file__)
    plugins_directory = os.path.join(script_directory, "plugins")
    writer_plugin = kernel.add_plugin(parent_directory=plugins_directory, plugin_name="WinePlugin")
    wine_name=input("Please enter the name of the wine: ")
    result = await kernel.invoke(writer_plugin["Somellier"], input=wine_name)

    print(result)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())