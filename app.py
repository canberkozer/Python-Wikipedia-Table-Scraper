import urllib.request
import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("http://www.wikizero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9Vbml0ZWRfU3RhdGVzX2NpdGllc19ieV9wb3B1bGF0aW9u")

source = BeautifulSoup(r.content,"html.parser")

table = source.find('table',attrs={"class":"wikitable sortable"})

links = table.find_all('a')

cities = []
for link in links:
    cities.append(link.get('title'))

print(cities)


df = pd.DataFrame()
df['City'] = cities

print(df)
