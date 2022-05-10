import socket

ip = '220.69.189.125'
port = 443

name = socket.getfqdn(ip)
print(name)

pro = socket.getservbyport(port)
print(pro)

url = '{}://'.format(socket.getservbyport(port))
url2 = name
print(url + url2)

print(socket.inet_aton(ip))
