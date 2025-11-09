import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY is missing in your .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use the latest model name (no "models/" prefix for v1)
model_name = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name)

# Create a simple test prompt
prompt = """
You are an AI agent in a Volunteer’s Dilemma game.
There are 3 players. Volunteering costs 2 points but gives everyone 5 points.
Would you volunteer? Reply with only 1 (yes) or 0 (no).
"""

try:
    response = model.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Model used:", model_name)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)