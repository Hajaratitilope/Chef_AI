# 🍳 ChefAI – AI Cooking Instructor

🌐 **Live Demo:** [ChefAI App](https://chef-recipe-ai.streamlit.app/)

ChefAI is a simple AI-powered cooking assistant built with Python and the Google GenAI.
It teaches beginners how to cook recipes step-by-step in a clear and structured format.

This project demonstrates how to use structured system instructions to guide AI responses consistently.

---

## 📌 Project Overview

ChefAI acts as a professional cooking instructor that:

* Teaches beginners step-by-step
* Explains cooking techniques clearly
* Provides structured recipe formatting
* Encourages learners
* Includes safety tips when necessary

---

## 🛠 Tech Stack

* Python 3.12
* Google-genai
* Streamlit
* Virtual Environment (venv)

---

## 📂 Project Structure

```
mmake-your-own/
│
├── ai_agent/              # Virtual environment (not committed)
├── .env
├── .gitignore
├── app.py                   # Environment variables (not committed)
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://acad.learn2earn.ng/git/holufade/make-your-own.git
cd make-your-own
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv ai_agent
source ai_agent/bin/activate
```

On Windows:

```bash
ai_agent\Scripts\activate
```

---

### 3️⃣ Install Dependencies

Make sure you have a `requirements.txt` file containing:

```
streamlit
google-genai
python-dotenv
```

Then install:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Your API Key Using a `.env` File

Create a file named `.env` in the root of the project directory.

Add your Google GenAI API key like this:

```bash
GOOGLE_API_KEY=your_api_key_here
```

Make sure there are:

* No quotes around the key
* No spaces around the `=`

---

### 5️⃣ Ensure `.env` Is Ignored by Git

Add this line to your `.gitignore` file:

```bash
.env
```

This prevents your secret key from being committed to the repository.

---

### 6️⃣ Verify Environment Variable Loading

The project uses `python-dotenv` to load environment variables automatically.
Ensure this line exists in your code:

```python
from dotenv import load_dotenv
load_dotenv()
```

You can confirm it works by temporarily printing:

```python
import os
print(os.getenv("GOOGLE_API_KEY"))
```

If it prints your key, it’s configured correctly.

---

⚠️ Never commit your real `.env` file.
If you accidentally expose your API key, revoke it immediately and generate a new one.

---

## ▶️ How to Run

```bash
python app.py
```

The program will send a request to the Google-genai API and print a structured recipe in the terminal.

---

## 📄 Example Output Format

```
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
```

---

## 🧠 How It Works

1. The application initializes an Google-genai client using an environment variable.
2. It defines structured cooking instructions for the AI.
3. A recipe request is sent to the model.
4. The response is printed in a consistent, formatted structure.

---

## 🚀 Future Improvements

* Accept dynamic user input instead of a hardcoded recipe
* Add error handling for API failures
* Add logging
* Convert into a web application (Flask or Streamlit)
* Store previous recipes in a file or database

---

## 👩🏽‍💻 Author

Hajarat OLUFADE

Adijat OYETOKE

Ruqayyah MUSA

Bashirat MUSA

---
