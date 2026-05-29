# Basic Web Scraper using BeautifulSoup and Requests

import requests
from bs4 import BeautifulSoup

print("===================================")
print("       BASIC WEB SCRAPER")
print("===================================")

# Website URL
url = "https://news.ycombinator.com/"

try:
    # Send request to website
    response = requests.get(url)

    # Check request status
    if response.status_code == 200:

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        print("\nTop News Headlines:\n")

        # Find headlines
        headlines = soup.find_all("span", class_="titleline")

        # Display headlines
        for index, headline in enumerate(headlines[:10], start=1):
            print(f"{index}. {headline.text}")

    else:
        print("Failed to retrieve webpage.")

# Handle connection errors
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
