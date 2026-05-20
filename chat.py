import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai_client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Add the user message
    conversation_messages.append(
        {"role": "user",
        "content": input_text}
    )

    # Get a completion
    completion = openai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # Your deployment name from .env
        messages=conversation_messages
    )
    assistant_message = completion.choices[0].message.content
    print("\nAssistant:", assistant_message)

    # Append the response to the conversation
    conversation_messages.append(
        {"role": "assistant", "content": assistant_message}
    )

#==========
# completion = openai_client.chat.completions.create(
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # Your deployment name from .env
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "When was Microsoft founded?"}
#     ]
# )

# print(completion.choices[0].message.content)

# #==================
# # Initial messages
# conversation_messages=[
#     {
#         "role": "system",
#         "content": "You are a helpful AI assistant that answers questions and provides information."
#     }
# ]

# # Add the first user message
# conversation_messages.append(
#     {"role": "user",
#     "content": "When was Microsoft founded?"}
# )

# # Get a completion
# completion = openai_client.chat.completions.create(
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # Your deployment name from .env
#     messages=conversation_messages
# )
# assistant_text = completion.choices[0].message.content
# print("Assistant:", assistant_text)

# # Append the response to the conversation
# conversation_messages.append(
#     {"role": "assistant", "content": assistant_text}
# )

# # Add the next user message
# conversation_messages.append(
#     {"role": "user",
#     "content": "Who founded it?"}
# )

# # Get a completion
# completion = openai_client.chat.completions.create(
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#     messages=conversation_messages
# )
# assistant_message = completion.choices[0].message.content
# print("Assistant:", assistant_text)

# # and so on...