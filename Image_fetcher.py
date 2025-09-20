import os
import requests
from urllib.parse import urlparse

def fetch_image():
    print("Ubuntu-Inspired Image Fetcher")
    print("The Wisdom of Ubuntu: 'I am because we are'\n")

    # Prompt the user for a URL
    url = input("Enter the image URL: ").strip()

    # Create directory for images
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    try:
        # Send a request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename is missing, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        # Full file path
        filepath = os.path.join(directory, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Image successfully downloaded and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("Error: The URL provided is invalid. Please provide a valid URL.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the internet. Please check your connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
