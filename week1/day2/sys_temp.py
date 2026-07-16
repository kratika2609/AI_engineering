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

role = "user"
prompt = "suggest me a name"
#system
message_system =  {
        "role":"system",
        "content":"you are a brand manager who suggests name for my food company,name should be one word"
    }


message =  {
        "role": role,
        "content": prompt
    }

messages = [message_system,message]
print("Messages Sent:\n")
for msg in messages:
    print(f"Role   : {msg['role']}")
    print(f"Content: {msg['content']}")
    print("-" * 30)

#temperature by default is 0    
response = client.chat.completions.create(model=model,messages=messages,temperature=2
)
#print(response)
print("\nAssistant Response:")
print(response.choices[0].message.content)
print('########################')
#print(response.choices[0].message.content)