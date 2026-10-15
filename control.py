import os
from typing import Literal
from pydantic import BaseModel
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("APIM_BASE_URL"),
    api_key=os.getenv("APIM_SUBSCRIPTION_KEY"),
    azure_deployment=os.getenv("OPENAI_MODEL"),
    api_version="2024-08-01-preview"
)

class IntentClassification(BaseModel):
    intent: Literal["research", "research and save to txt", "find opening times"]
    confidence: float
    reasoning: str

query = input("What can I help you with? ")

response = client.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {
            "role": "system", 
            "content": 
            """
            Classify user input into one of the three categories: 
            'research', 'research and save to txt', or 'find opening times'. 

            Provide your reasoning and confidence level. 
            """
        },
        {
            "role": "user", 
            "content": query
        }
    ],
    response_format=IntentClassification
)

classification = response.choices[0].message.parsed
intent = classification.intent

print(f"Intent: {intent}", end="\n")
print("Confidence:", classification.confidence, end="\n")
print("Reasoning:", classification.reasoning)

def handle_research():
    print("Handling research intent...")

def handle_research_and_save():
    print("Handling research and save to txt intent...")

def handle_find_opening_times():
    print("Handling find opening times intent...")

def route_intent(intent: str):
    intents = {
        "research": handle_research,
        "research and save to txt": handle_research_and_save,
        "find opening times": handle_find_opening_times
    }
        
    return intents.get(intent, lambda: print("Invalid intent"))()


route_intent(intent)
