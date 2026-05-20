import os
from openai import OpenAI
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()  # Load environment variables from .env file

# Create the client
client = TextAnalyticsClient(endpoint=os.getenv("AZURE_LANGUAGE_ENDPOINT")
                             , credential=AzureKeyCredential(os.getenv("AZURE_OPENAI_API_KEY")))

# Make a request using the client for language detection
text = "¡Hola! Me llamo Josefina y vivo en Madrid, España."
result = client.detect_language([text])[0]

# Print the results
print(f"Language      : {result.primary_language.name}")
print(f"ISO code      : {result.primary_language.iso6391_name}")
print(f"Confidence    : {result.primary_language.confidence_score:.2f}")