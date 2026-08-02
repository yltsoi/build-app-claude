import anthropic
from fastapi import FastAPI

app = FastAPI()
client = anthropic.AsyncAnthropic()

async def ask_claude(prompt: str) -> str:
    messages = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return messages.content[0].text

@app.post("/summarize")
async def summarize(text: str):
    result = await ask_claude(f"Please summarize the following text: {text}")
    return {"summary": result}

