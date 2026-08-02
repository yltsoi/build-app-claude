import asyncio, anthropic
from dotenv import load_dotenv
load_dotenv()   


client = anthropic.AsyncAnthropic()

async def classify_text(prompt: str) -> str:
    messages = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system = "Reply with one work: positive, negative, or neutral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return messages.content[0].text

    async def run_batch(docs: list[str], limit: int = 5) -> list[str]:
        sem = asynci.Semaphore(limit)
        async def counded(doc: str) -> str:
            async with sem:
                return await classify_text(doc  )
                return await asyncio.gather(*(counded(doc) for doc in docs))

                docs = ["Great product!", "Shipment was late", "Item arrived fine"]
                result = asyncio.run(run_batch(docs))
                print[results]

        
