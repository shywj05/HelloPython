import requests
import json

url = "https://dapi.kakao.com/v2/search/image"
queryString = {"query":"남주혁"}
header = {'authorization':'KakaoAK b261567bd62d4bfb4862f1d558d65f92'}
r = requests.get(url, headers=header, params=queryString)

# check = json.loads(r.text)
# print(check)
# 
# for i in check['documents']:
#     print(i['collection'], i['datetime'], i['display_sitename'], i['doc_url'], i['height'], i['image_url'], i['thumbnail_url'], i['width'])

myjson = json.loads(r.text)
print(myjson)

for i in myjson['documents']:
    print(i['collection'], end="\t")
    print(i['datetime'], end="\t")
    print(i['display_sitename'], end="\t")
    print(i['doc_url'], end="\t")
    print(i['height'], end="\t")
    print(i['image_url'], end="\t")
    print(i['thumbnail_url'], end="\t")
    print(i['width'])
    
     
