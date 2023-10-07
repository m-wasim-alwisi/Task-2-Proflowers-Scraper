import requests
from bs4 import BeautifulSoup
import json

# Set your custom user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Send a GET request to the URL with the custom user agent
url = "https://www.proflowers.com/blog/types-of-flowers"

headers = {'User-Agent': user_agent}

response = requests.get(url, headers=headers)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <td> elements
td_elements = soup.find_all('td', class_='article-sections_tableCell__2HBAw')

# Initialize a list to store the extracted data
flowers = []

# Extract the data
for td in td_elements:
    # Find the <b> elements within the <td>
    b_elements = td.find_all('b')

    # Initialize a dictionary to store the flower data
    flower_data = {}

    # Extract the data from each <b> element
    for b in b_elements:
        if b.text == "Sun Needs":
            flower_data["Sun Needs"] = b.find_next_sibling('br').next_sibling.strip()
        elif b.text == "Soil Needs":
            flower_data["Soil Needs"] = b.find_next_sibling('br').next_sibling.strip()
        elif b.text == "Zones":
            flower_data["Zones"] = b.find_next_sibling('br').next_sibling.strip()
        elif b.text == "Height":
            flower_data["Height"] = b.find_next_sibling('br').next_sibling.strip()
        elif b.text == "Blooms in":
            # Check if there are multiple lines for 'Blooms in'
            if b.find_next_sibling('br').next_sibling:
                flower_data["Blooms in"] = b.find_next_sibling('br').next_sibling.strip()
            else:
                flower_data["Blooms in"] = b.find_next_sibling('br').next_sibling.strip()
                flower_data["Blooms in"] += " - " + b.find_next_sibling('br').next_sibling.next_sibling.strip()
        elif b.text == "Features":
            flower_data["Features"] = b.find_next_sibling('br').next_sibling.strip()

    # Add the flower data to the list if it is not empty
    if flower_data:
        flowers.append(flower_data)

# Convert the list to JSON
output_json = json.dumps(flowers, indent=4)

# Print the JSON output
with open('flower_data.json', 'w') as json_file:
    json.dump(flowers, json_file, indent=4)
