# libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Header to access the website
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# Scraping from houses in Corvallis, Or
url= "https://www.realtor.com/realestateandhomes-search/Corvallis_OR"
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')
# Find all in container <li> with the class that is assigned to all listing cards on the page
lists = soup.find_all('li', class_= "jsx-1881802087 component_property-card")

# Open csv file to write the data to
with open('real-estate.csv', 'w', encoding='utf8', newline='') as f:
    for list in lists:
        price = list.find('span', class_= "Price__Component-rui__x3geed-0 gipzbd").text
        location = list.find('div', class_= "jsx-1982357781 address ellipsis srp-page-address srp-address-redesign").text
        area = list.find('li', class_= "jsx-946479843 prop-meta srp_list").text
        info =  [price, location, area]
        
        # Pandas dataframe for the data
        df = pd.DataFrame(info)
        # Appends dataframe to the csv file with index set to true for organization
        df.to_csv('real-estate.csv', index=True, mode='a', header=False)