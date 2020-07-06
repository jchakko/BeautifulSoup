from bs4 import BeautifulSoup
import requests

url = "https://www.nps.gov/state/fl/index.htm"
soup = BeautifulSoup(requests.get(url).content)

florida = soup.find(id = "parkListResultsArea")
parks = florida.find_all('h3')

for park in parks:
    link = park.find('a')
    print(link.get_text())