import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "https://demo-azure-openai-nguyen.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview",
)


# Function to interact with Azure OpenAI chat completion
def ai_chat(user_message):
    # Define the message sequence for the chat
    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": user_message}
    ]

    # Create a completion using the Azure OpenAI client
    completion = client.chat.completions.create(
        model=deployment,  # Specify the deployment model
        messages=message_text,  # Pass the list of messages
        max_tokens=800,  # Limit the response length to 800 tokens
        temperature=0.7,  # Set the response randomness
        top_p=0.95,  # Use nucleus sampling
        frequency_penalty=0,  # No penalty for repeating tokens
        presence_penalty=0,  # No penalty for repeating topics
        stop=None,  # No specific stop sequences
        stream=False  # Response is returned as a single output
    )

    return completion.choices[0].message.content


# Welcome message
print("Welcome! How can I help you today?")

# Main loop to continuously interact with the user
while True:
    user_message = input(">> ")  # Get input from the user
    completion = ai_chat(user_message)  # Call the ai_chat function with the user's message
    # Extract and print the assistant's response from the completion object
    print(completion)

#completion = client.chat.completions.create(
#    model=deployment,
#    messages=[
#        {
#            "role": "user",
#            "content": "What are the differences between Azure Machine Learning and Azure AI services?"
#        }],
#    max_tokens=800,
#    temperature=0.7,
#    top_p=0.95,
#    frequency_penalty=0,
#    presence_penalty=0,
#    stop=None,
#    stream=False
#)
#print(completion.to_json())