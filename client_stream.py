import anthropic
from dotenv import load_dotenv    
load_dotenv()

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "What is the Claude API?"
        }
    ]
) as stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)