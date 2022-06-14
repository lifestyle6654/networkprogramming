# 웹 클라이언트

import requests

url = 'http://localhost:8080'
rsp = requests.get(url)
print(rsp.status_code)
print(rsp.headers)
print(rsp.text)