import requests
from bs4 import BeautifulSoup

URL = 'http://192.168.41.115:7070/HELLOWEB/tel_list.jsp'
response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# print(soup.select('td'))

tds = soup.select('td')

for i in tds:
    print(i.text)

    




