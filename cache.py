import anthropic, hashlib
from dotenv import load_dotenv
load_dotenv()

client = anthropic.AsyncAnthropic()
cache: dict = {}

def ask(prompt: str) -> str:
    key = hashlib.sha256(prompt.encode()).hexdigest()
    if key in cache:
        return cache[key]
        messages = client.messages.create(     
            model="claude-haiku-4-5",
            max_tokens=256,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        cache[key] = messages.content[0].text   
        return cache[key]

print("First call (hits cache):")
print(ask("What is the Claude API?"))
print("Second call (hits cache):")  
print(ask("What is the Claude API?"))

