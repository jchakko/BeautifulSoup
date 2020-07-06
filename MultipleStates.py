from bs4 import BeautifulSoup
import requests

# Full results container
results = []

# Retrieve all parks from a state's page
def parse_state(url):
    soup = BeautifulSoup(requests.get(url).content)
    state = soup.find(id = "parkListResultsArea")
    parks = state.find_all('h3')
    return parks

# Transfrom a BeautifulSoup tag to a dictionary
def parse_park(park, state):
    tag = park.find('a')
    url = tag['href']
    name = tag.get_text()
    park_dict = {"Name": name, "State": state, "URL": url}
    return park_dict

url = "https://www.nps.gov/state/PLACEHOLDER/index.htm"
states = ["fl", "vt", "de", "wi"]

# For every state in the above list
for state in states:
    # Retrieve all parks from the state's page
    state_url = url.replace("PLACEHOLDER", state)
    state_results = parse_state(state_url)
    
    # For every park in the state's page
    for park in state_results:
        # Transform the BeautifulSoup tag to a dictionary and append to the results
        park_result = parse_park(park, state)
        results.append(park_result)
    
import csv
with open('export.csv', 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)