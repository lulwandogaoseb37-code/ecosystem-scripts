from datetime import datetime

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
    notes = input("Key insight from this session: ")
    question = input("What question does this raise? ")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = f"""
---
Date: {timestamp}
Subject: {subject}
Topic: {topic}
Insight: {notes}
Question raised: {question}
---
"""
    
    with open(filename, "a") as f:
        f.write(entry)
    
    print(f"\nSession logged to {filename}")

log_session()
