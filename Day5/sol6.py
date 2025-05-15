# Challenge 6: Use the requests module to fetch and display data from a public API (e.g., JSONPlaceholder).

import requests 
import json

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON data
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    return None

def display_data(data):
    if data:
        print(json.dumps(data, indent=4))  # Pretty-print JSON data
    else:
        print("No data to display.")
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data_from_api(url)
    display_data(data)

