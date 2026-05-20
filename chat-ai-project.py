# Before running the sample:
#    pip install azure-ai-projects>=2.0.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

project_client = AIProjectClient(
    endpoint=os.getenv("AZURE_OPENAI_PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential(),
)

my_agent = "agent-test"
my_version = "1"

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")



