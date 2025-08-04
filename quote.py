import requests
import json

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        # The API endpoint for a random quote
        url = "https://api.quotable.io/random"
        
        # Make the GET request
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        response.raise_for_status()
        
        # Parse the JSON response
        quote_data = response.json()
        
        # Extract the content and author
        content = quote_data.get("content", "No quote content found.")
        author = quote_data.get("author", "Unknown author")
        
        # Print the formatted quote
        print("\n" + "—" * 60)
        print(f'"{content}"')
        print(f"- {author}")
        print("—" * 60 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError:
        print("Failed to decode the server's response.")

if __name__ == "__main__":
    get_random_quote()