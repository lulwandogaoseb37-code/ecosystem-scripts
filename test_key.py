import requests
import os
API_KEY = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": "Say: API connection successful"}
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print(data)
