import requests
from bs4 import BeautifulSoup

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php'
response = requests.get(URL)
response.encoding = 'euc-kr'

html = response.text
soup = BeautifulSoup(html, 'html.parser')

tds = soup.select('.st2')

for i in tds:
    print(i.text,end="\t")
    print(i.find("a")["title"], end="\t")
    print(i.parent.find_all("td")[1].text)
    
