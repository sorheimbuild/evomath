"""
Query Groq API (Llama) for feedback on EvoMath
"""
import os
import requests
from groq import Groq

# First, let's see what models are available
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not set in environment")
    exit(1)

# Check available models
url = "https://api.groq.com/openai/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(url, headers=headers)
if response.ok:
    models = response.json().get("data", [])
    print("Available models:")
    for m in models[:15]:
        print(f"  - {m['id']}")
else:
    print(f"Could not fetch models: {response.text}")

# Read the evaluation doc
with open("FOR_AI_EVALUATION.md", "r") as f:
    eval_doc = f.read()

prompt = f"""You are reviewing a project called EvoMath. Read this summary and answer:

1. Is this a valid approach for symbolic regression?
2. What's the most interesting/improving?
3. What would make it credible?
4. Is the SHA256 idea worth exploring?

---SUMMARY---
{eval_doc}
"""

try:
    client = Groq(api_key=api_key)
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # or use a model from the list
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    print("\n--- Groq Response ---")
    print(chat.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
