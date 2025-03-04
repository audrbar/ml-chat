#!/usr/bin/env python  # Use the system's Python 3 interpreter

import os
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Generate a chat completion
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Please name capital of Great Britain"}]
)

# Print the result - Structure mode in Openai
print(f"\n{completion.choices[0].message.content}\n")
