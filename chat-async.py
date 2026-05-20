import asyncio
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = AsyncOpenAI(
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

async def main():
    response = await client.responses.create(
        model="gpt-4.1",
        input="Explain quantum computing briefly."
    )
    print(response.output_text)

asyncio.run(main())