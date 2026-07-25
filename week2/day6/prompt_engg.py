import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

load_dotenv()

#get API key
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Not found API key")

#create Groq client
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

def llm_ans(prompt):
    message = {
        "role": "user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

# bad_prompt = """
# This is a user complaint:
# My laptop is not working.
# Classify this.
# """

good_prompt = """
This is a user complaint:
I have bought my laptop from HP store. And its done only 6 months and it is not working properly. My laptop storage is full automatically even i havenot downloaded anything.
Plz fix this.
"""
print(llm_ans(good_prompt))