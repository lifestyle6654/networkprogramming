# requests 모듈: DELETE, HEAD
# requests.delete() -> 자원 삭제
# requests.head() -> HTTP Response의 헤더만 가져옴

import requests

rsp = requests.delete('https://httpbin.org/delete')
print(rsp.text)
rsp = requests.head('https://httpbin.org/get')
print(rsp.headers)
print(rsp.text)