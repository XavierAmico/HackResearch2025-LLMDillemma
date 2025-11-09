import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiAgent:
    def __init__(self, name, personality="neutral", model_name="gemini-flash-latest"):
        self.name = name
        self.personality = personality
        self.model_name = model_name

        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing API key.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def decide(self, n_players, reward, cost, others_last_actions):
        """Ask Gemini for a probability to volunteer (0–1)."""
        prompt = f"""
        You are playing the Volunteer’s Dilemma.
        Personality: {self.personality}

        Rules:
        - There are {n_players} players.
        - Reward if at least one volunteers: {reward}.
        - Cost to volunteer: {cost}.
        - Last round, other players chose: {others_last_actions}.

        Respond with a single floating-point number between 0 and 1
        representing the probability that you will volunteer this round.
        Only output the number.
        """

        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            prob = float(text)
            if not 0 <= prob <= 1:
                raise ValueError("Out of range")
            return prob
        except Exception:
            # Fallback random
            return random.random()