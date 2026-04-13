import requests
from datetime import datetime

import os
API_KEY = os.environ.get("GROQ_API_KEY")
def get_ai_questions(subject, topic, insight):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": f"I am a first year university student studying {subject}. I just studied {topic} and my key insight was: {insight}. Generate exactly 3 deep follow up questions that will push my understanding further. Be specific to what I wrote. Number them 1, 2, 3."
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data["choices"][0]["message"]["content"]

def log_session():
    print("\nSubjects:")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Biology")
    print("4. Mathematics")
    print("5. Other")
    
    choice = input("\nSelect subject number: ")
    
    subjects = {
        "1": "Physics",
        "2": "Chemistry",
        "3": "Biology",
        "4": "Mathematics",
        "5": "Other"
    }
    
    subject = subjects.get(choice, "Other")
    filename = f"{subject.lower()}_log.txt"
    
    topic = input("What topic are you studying? ")
    insight = input("Key insight from this session: ")
    question = input("What question does this raise? ")
    
    print("\nGenerating follow up questions...")
    ai_questions = get_ai_questions(subject, topic, insight)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = f"""
---
Date: {timestamp}
Subject: {subject}
Topic: {topic}
Insight: {insight}
Your question: {question}

AI Follow Up Questions:
{ai_questions}
---
"""
    
    with open(filename, "a") as f:
        f.write(entry)
    
    print("\nAI Follow Up Questions:")
    print(ai_questions)
    print(f"\nSession logged to {filename}")

log_session()
