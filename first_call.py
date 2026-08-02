import anthropic
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Client()

messages = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens = 256,
    messages=[
        {
            "role": "user",
            "content": "What is the Claude API ?"
        }
    ]
)

print(messages.content[0].text)