import urllib.request as req
from urllib.parse import urlparse
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com/"

mem = req.urlopen(url)

print(type(mem))
print('--------------------')
print("geturl :",mem.geturl())
print('--------------------')
print("status :",mem.status)
print('--------------------')
print("headers :",mem.getheaders())
print('--------------------')
print("info :",mem.info(),"\n")
print('--------------------')
print("getcode :",mem.getcode())
print('--------------------')
print("read :",mem.read(10).decode('utf-8'))
print('--------------------')
print(urlparse('http://www.encar.co.kr?test=test').query)
