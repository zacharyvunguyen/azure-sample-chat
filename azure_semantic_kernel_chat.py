from dotenv import load_dotenv
import os
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
import asyncio

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

prompt = """
I need to understand what are the variables involved in making outstanding espresso besides a good machine. For example what is the combination of roast, grind, tamp, and water temperature. Include 3 practical steps to practice and improve each variable."""

prompt_template_config = PromptTemplateConfig(
    template=prompt,
    name="tldr",
    template_format="semantic-kernel",
)

function = kernel.add_function(
    function_name="tldr_function",
    plugin_name="tldr_plugin",
    prompt_template_config=prompt_template_config,
)

# Run your prompt
# Note: functions are run asynchronously
async def main():
    result = await kernel.invoke(function)
    print(result) # => Robots must not harm humans.

if __name__ == "__main__":
    asyncio.run(main())
# If running from a jupyter-notebook:
# await main()