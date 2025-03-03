#!/usr/bin/env python  # Use the system's Python 3 interpreter

import requests  # Import the requests library to make HTTP requests

# Function to fetch todos from the API and print the first 10 todos
def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"  # API endpoint for todos
    response = requests.get(url)  # Send a GET request to the API

    if response.status_code == 200:  # Check if the request was successful
        todos = response.json()  # Parse the JSON response into a Python list

        # Iterate over the first 10 todos and print their details
        for i, todo in enumerate(todos[:10], start=1):
            print(f"{i}. ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        # Print an error message if the request fails
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Run the script only if it's executed directly
if __name__ == "__main__":
    fetch_todos()
