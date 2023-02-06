import requests
from bs4 import BeautifulSoup

# create a session
session = requests.Session()

# fetch the webpage
url = 'https://vuzopedia.ru/'
response = session.get(url)

# parse the html
soup = BeautifulSoup(response.text, 'html.parser')

# get the universities
universities = soup.find_all('a', class_='link_lg')

# store the data
data = []
for university in universities:
    name = university.text
    link = university.get('href')
    data.append({'name': name, 'link': link})

# print the data
print(data)