import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env if you used Option B
load_dotenv()

# 1. Initialize the client
# Make sure you have run: export GEMINI_API_KEY="your_actual_key" in your terminal first.
client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)