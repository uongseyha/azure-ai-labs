import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# # Get response using the code_interpreter tool
# response = client.responses.create(
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#     instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
#     input="What is the square root of 16?",
#     tools=[{"type": "code_interpreter",
#             "container": {"type": "auto"}}]
# )

# # Get response using the web_search tool
# response = client.responses.create(
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#     instructions="You are an AI assistant. Use web search when current information is required.",
#     input="What are three major announcements from Microsoft Build this week?",
#     tools=[{"type": "web_search"}]
# )

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the maximum amount I can claim for a taxi ride?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)

print(response.output_text)