import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

prompts = [
    "Hi!",
    "Give time complexity of binary search",
    "Who is PM of India?"
]

for prompt in prompts:

    message = {
        "role": "user",
        "content": prompt
    }

    response = client.chat.completions.create(
        model=model,
        messages=[message]
    )

    usage = response.usage

    print("\n-----------------------------")
    print("Prompt:", prompt)
    print("Response:", response.choices[0].message.content)

    print(
        "Prompt tokens:", usage.prompt_tokens,
        "Completion tokens:", usage.completion_tokens,
        "Total tokens:", usage.total_tokens
    ) 