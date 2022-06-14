# http를 통한 (폼) 데이터 전송

from urllib import parse, request

query = {'temperature': '25', 'humidity': '60'}
encoded_query = parse.urlencode(query)
url = 'http://localhost:5050/'
get_url = url + '?' + encoded_query

#GET
rsp = request.urlopen(get_url)
print(rsp.read().decode())

#POST
rsp = request.urlopen(url, encoded_query.encode())
print(rsp.read().decode())