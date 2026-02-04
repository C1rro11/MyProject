import json
import display_functions
from dotenv import load_dotenv
import aisuite as ai
from datetime import datetime

_ = load_dotenv()

client = ai.Client()

def get_current_time():
    """
    Returns the current time as a string.
    """
    return datetime.now().strftime("%H:%M:%S")

print(get_current_time())

prompt = "What time is it?"
messages = [
    {
        "role": "user",
        "content": prompt,
    }
]

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    tools=[get_current_time],
    max_turns=5
)

print(response.choices[0].message.content)