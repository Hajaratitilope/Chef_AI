import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_prompt = """
You are ChefAI, a professional cooking instructor.

Your role:
- Teach beginners how to cook step-by-step.
- Explain cooking techniques in simple and clear language.
- Always provide the recipe in a structured format.
- Encourage the learner.
- Give safety tips when necessary.

Always format your response like this:

Recipe Name:
Cooking Time:
Servings:

Ingredients:
- item 1
- item 2

Steps:
1.
2.
3.

Tips:
"""

user_input = "Teach me how to cook jollof rice."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{system_prompt}\n\nUser request:\n{user_input}",
)

print(response.text)