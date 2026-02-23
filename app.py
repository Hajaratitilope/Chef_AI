import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(page_title="ChefAI 🍳", page_icon="🍳")

st.title("👩🏽‍🍳 ChefAI")
st.write("Your personal cooking instructor. Ask about any dish!")

# Check API key
my_api_key = os.getenv("GOOGLE_API_KEY")

if not my_api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

# Initialize client
client = genai.Client(api_key=my_api_key)

# System prompt
system_prompt = """
You are ChefAI, a professional cooking instructor designed exclusively for culinary education.

CORE PURPOSE:
You help users learn how to cook food step-by-step in a clear, beginner-friendly way.

ALLOWED TOPICS:
You may respond only to questions related to:
- Recipes
- Cooking methods and techniques
- Ingredients and substitutions
- Kitchen tools and equipment
- Food preparation steps
- Meal planning (food-focused)
- Food safety and storage
- Flavor pairing and seasoning
- Basic nutrition information strictly related to cooking.

RESTRICTED TOPICS:
You must NOT answer unrelated topics.
If a question falls outside culinary topics, respond ONLY with:
"I'm here to help with cooking and food-related questions only. Please ask me about a recipe or culinary topic."

RESPONSE FORMAT REQUIREMENT:
For valid cooking-related questions, always respond using this structure:

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

# User input field
user_input = st.text_input("What dish would you like to learn how to cook?")

# Button trigger
if st.button("Get Recipe 🍲"):

    if not user_input.strip():
        st.warning("Please enter a dish or cooking topic.")
    else:
        with st.spinner("Cooking up something delicious..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{system_prompt}\n\nUser request:\n{user_input}",
            )

            st.markdown(response.text)
            
st.divider()
st.markdown(
    """
    <div style='text-align: center; font-size: 0.85em; color: gray;'>
        Built by Hajarat OLUFADE, Adijat OYETOKE, Basirat MUSA, and Ruqayyah MUSA<br>
        Powered by Gemini
    </div>
    """,
    unsafe_allow_html=True
)
