import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

# Pydantic model
class Ticket(BaseModel):
    name: str
    email: str
    issue: str


# Generate JSON schema
schema = Ticket.model_json_schema()

# Response format
response_format = {
    "type": "json_object"
}

# System prompt
system_prompt = f"""
Extract the personal information from the customer ticket strictly based on this schema:

{schema}

Return only valid JSON.
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

# Customer ticket
text = """
Hello, my name is Kratika. I am from Kanpur.
I have an iPhone which is not working.
My contact no is 45678.
"""

prompt = f"""
This is a customer ticket.
Please extract the following information:

{text}
"""

message = {
    "role": "user",
    "content": prompt
}

# Complete messages list
messages = [message_system, message]

# API call
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

# Print output
print(response.choices[0].message.content)