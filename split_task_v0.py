# Import the 'os' module to access environment variables like your API key
import os

# Import the 'json' module to format and pretty-print the output
import json

# Import the OpenAI client library to send requests to GPT models
import openai

# Load your OpenAI API key from an environment variable called "OPENAI_API_KEY"
# This keeps your secret key out of the source code
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ask the user to type in a high-level goal
# Example: "I want to prepare my tax return"
goal = input("Your goal: ")

# Define the system message that sets the assistant's behavior
# Here: act like a task planning assistant
system = "You are TaskPlannerGPT. Break goals into 3–7 concrete steps."

# Send the chat request to the OpenAI API using the gpt-4o-mini model
# The model receives both system and user messages
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system},  # System prompt (defines the assistant's identity)
        {"role": "user", "content": f"Goal: {goal}. Return JSON array only."}  # User's goal
    ],
)

# The response from the model is expected to be a JSON-formatted list of subtasks
# This line prints it in a readable format
print(json.dumps(response.choices[0].message.content, indent=2))
