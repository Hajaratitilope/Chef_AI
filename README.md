# 🍳 ChefAI – AI Cooking Instructor

ChefAI is a simple AI-powered cooking assistant built with Python and the OpenAI API.
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
* OpenAI Python SDK
* Virtual Environment (venv)

---

## 📂 Project Structure

```
make-your-own/
│
├── ai_agent/          # Virtual environment
├── app.py             # Main application file
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://your-gitea-url/make-your-own.git
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

```bash
pip install openai
```

---

### 4️⃣ Set Your OpenAI API Key

Linux / macOS:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Windows (PowerShell):

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Verify that it is set:

```bash
echo $OPENAI_API_KEY
```

⚠️ Do NOT commit your API key to the repository.

---

## ▶️ How to Run

```bash
python app.py
```

The program will send a request to the OpenAI API and print a structured recipe in the terminal.

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

1. The application initializes an OpenAI client using an environment variable.
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
