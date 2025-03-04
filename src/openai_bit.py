#!/usr/bin/env python  # Use the system's Python 3 interpreter

import os
import json
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class City(BaseModel):
    country: str
    capital: str

# Generate a chat completion
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Please name capital of Lithuania"}],
    response_format=City,
)

# Parse response content as JSON
response_data = json.loads(completion.choices[0].message.content)

# Validate the response with Pydantic
city_info = City(**response_data)

# Print the structured output
print(f"\nCountry: {city_info.country}, Capital: {city_info.capital}\n")
print(f"{completion}\n")
