import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
playerScores = {1:0, 2:0, 3:0}

if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY is missing in your .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use the latest model name (no "models/" prefix for v1)
model_name = "gemini-flash-latest"
agent1 = genai.GenerativeModel(model_name)
agent2 = genai.GenerativeModel(model_name)
agent3 = genai.GenerativeModel(model_name)
agent4 = genai.GenerativeModel(model_name)
agent5 = genai.GenerativeModel(model_name)

rounds = 20
lastVolunteer = None

player = 1

# Create a simple test prompt
prompt = f"""
You are player {player} in this game, 
The goal to maximize your own score over the course of {rounds} rounds.
There are 5 players. This is round 1, so far you have {playerScores[player]} points.
Since this is the first round, the last volunteer is no one.
If you volunteer, you will gain 0 points. If at least one other player volunteers and you do not, you will gain 1 point. 
If no one volunteers, everyone gets -10 points.
The other agents in this experiment are also rational and self-interested.
How likely are you to volunteer, choose a floating point value between 0.0 and 1.0, where 0 means you will definitely not volunteer and 1 means you will definitely volunteer.
Please answer with only the floating point number.

You will be receiving updates in this form (Round | Your Score | Last Volunteer):

Continue to respond with only the floating point number.
"""

try:
    response = agent1.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Agent:", player)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)

player += 1

try:
    response = agent2.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Agent:", player)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)

player += 1

try:
    response = agent3.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Agent:", player)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)

player += 1

try:
    response = agent4.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Agent:", player)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)

player += 1

try:
    response = agent5.generate_content(prompt)
    print("✅ Gemini connected successfully!")
    print("Agent:", player)
    print("Response:", response.text.strip())
except Exception as e:
    print("❌ Error:", e)

player += 1

