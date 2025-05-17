
import requests
import json

url = "https://fakerestapi.azurewebsites.net/api/v1/Books"  # Replace with the actual URL of your FastAPI endpoint

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        top_10_records = data[:10]  # Slice the list to get the first 10 elements

        if top_10_records:
            print("Top 10 Records:")
            for item in top_10_records:
                item_id = item.get("id")
                description = item.get("description")
                text = item.get("excerpt")

                print(f"\nID: {item_id}")
                print(f"Description:\n{description[:50]}...")  # Display first 50 characters of description
                print(f"Text (Excerpt):\n{text[:50]}...")      # Display first 50 characters of excerpt
        else:
            print("The response list is empty.")
    else:
        print("The response is not a list.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError:
    print("Failed to decode the JSON response.")