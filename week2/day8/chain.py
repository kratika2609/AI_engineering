import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

JD = """
We are hiring a backend Python developer.
Requirements:
- Python
- Django or FastAPI
- PostgreSQL
- Docker
- AMS 
- REST APIs
- Min 2+ years of experience
"""

RESUME = """
Name: Kratika Singh
Experience: 3 years of experience
Skills: Python, FastAPI, Docker, MySQL, Git
Projects: Built a food delivery backened using MySQL and FASTAPI
Deployed applications using Docker.

"""

def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role":"system",
        "content":system_prompt
    }
    user_msg = {
        "role":"user",
        "content":user_prompt
    }

    messages=[sys_msg, user_msg]
    response = client.chat.completions.create(messages=messages,model=model)
    answer = response.choices[0].message.content  
    return answer

def step1_res_extract(RESUME):
    #extract skills from resume
    print("Step 1")
    system_prompt = f"""
    You are a professional HR assisstant. Extract the skills from the candidates resume provided.
    Only return the skills not other informations. Do not invent any skills by yourself.
    """   
    user_prompt = f"""
    Extract the skills from this resume
    {RESUME}
    """ 
    return ask_llm(system_prompt, user_prompt)


def step2_JD_extract(JD):
    #extract skills from resume
    print("Step 2")
    system_prompt = f"""
    You are a professional HR assisstant. Extract the skills from the job description provided.
    Only return the skills not other informations. Do not invent any skills by yourself.
    """   
    user_prompt = f"""
    Extract the skills from the job description
    {JD}
    """ 
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate, JD):
    print("Step 3")
    system_prompt = """
    You are a professional HR assisstant. Compare the skills of candidate and the skilss provided in the job description and produce a final score list between 1 and 100.
    also produce a short verdict whther the candidate is a good fit for the role.
    """ 
    user_prompt = f"""
    Compare and match the skills.
    JD:
    {JD}
    Candidate:
    {candidate}

    """
    return ask_llm(system_prompt, user_prompt)

candidate = step1_res_extract(RESUME)
print(candidate)
sleep(2)
jd=step2_JD_extract(JD)
print(jd)
sleep(2)
score=step3_match(candidate,jd)
print(score)
