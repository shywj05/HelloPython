import requests
from bs4 import BeautifulSoup
import cx_Oracle
import datetime


URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php'
response = requests.get(URL)
response.encoding = 'euc-kr'

html = response.text
soup = BeautifulSoup(html, 'html.parser')

tds = soup.select('.st2')

con = cx_Oracle.connect("python/python@localhost:1521/xe")
cs = con.cursor()
sql = "INSERT INTO STOCK VALUES (:1, :2, :3, :4)"
s_intime = datetime.datetime.now().strftime("%y%m%d.%h%m")

for i in tds:
    s1 = i.text
    s2 = i.find("a")["title"]
    s3 = i.parent.find_all("td")[1].text.replace(',','')
    cs.execute(sql,(s2,s1,s3,s_intime))



print(s1)
print(s2)
print(s3)

con.commit()
cs.close()
con.close()
    
    

    
    
