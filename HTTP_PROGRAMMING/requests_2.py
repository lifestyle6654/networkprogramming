# requests 모듈: POST
# 데이터를 서버로 전송(자원 생성)

import requests

url = 'https://httpbin.org/post'
data = {'IoT': '2017'}
rsp = requests.post(url, data=data)
print(rsp.text)
rsp = requests.post(url, json=data)
print(rsp.text)
files = {'file': open('iot.png', 'rb')}
rsp = requests.post(url, files=files)
print(rsp.text)