import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env 
load_dotenv()

# 1. Initialize the client
client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)
