#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://copyassingnment.com/author/admin/'

res = requests.get(url).content

soup = BeautifulSoup(res,'html.parser')

links = soup.find_all('a')

for link in links:
	print(link['href']) 
