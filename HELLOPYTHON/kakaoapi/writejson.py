# -*- conding: [utf-8] -*-
import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'af8890c3a25e36b8a67c5e65775bfc34'
redirect_uri = 'https://localhost.com'
authorize_code = 'OgMrDosFGpwMldUVprLOlpw3ccarxWZKByM8bg6BQdhGhQ1HbfDPRdzsBfTPkrgKiqjuQgo9dNsAAAF39pnPHg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

import json

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
    
# https://kauth.kakao.com/oauth/authorize?client_id=af8890c3a25e36b8a67c5e65775bfc34&redirect_uri=https://localhost.com&response_type=code&scope=talk_message,friends