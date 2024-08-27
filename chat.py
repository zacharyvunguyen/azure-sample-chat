import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")


def ai_chat(user_message):
    message_text = [
       {"role":"system","content":"You are an AI assistant that helps people find information."},
       {"role": "user", "content": user_message}
    ]

    completion = openai.ChatCompletion.create(
      engine="demo-alfredo",
      messages=message_text,
      temperature=0.7,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )
    return completion


print("Welcome! how can I help you today?")

while True:
    user_message = input(">> ")
    completion = ai_chat(user_message)
    # Completion will return a response that we need to use to get the acctual string
    print(completion['choices'][0]['message']['content'])
