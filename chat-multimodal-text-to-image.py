import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("FOUNDRY_KEY"),
    base_url=os.getenv("ENDPOINT"),
)

prompt = "A modern flat illustration of a robot holding a potted plant, clean vector style, pastel colors."

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # your deployment name in Foundry
    input=prompt,
    tools=[{"type": "image_generation"}],
)

image_base64 = next(
    item.result for item in response.output
    if item.type == "image_generation_call"
)

with open("foundry_generated.png", "wb") as f:
    f.write(base64.b64decode(image_base64))

print("Saved: foundry_generated.png")