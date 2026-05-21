import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("FOUNDRY_KEY"),
    base_url=os.getenv("ENDPOINT"),
)

image_url = "https://plus.unsplash.com/premium_photo-1778531802673-11cbd1abe5b8?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What is in this image? Provide 3 bullet points."},
                {"type": "input_image", "image_url": image_url}
            ],
        }
    ],
)

print(response.output_text)