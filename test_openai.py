"""
@arshankar11 / Delhi / 22Sep26
Test OpenAI API key

"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the client with your key
client = OpenAI()

# Test it
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the capital of India?"}]
)
print(response.choices[0].message.content)

