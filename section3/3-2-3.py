import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
#print(r.text) #보기에는 json
#print(r.encoding) encoding결과가 none임 -> utf8로 인코딩해줘야함
#print(r.json())
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = json.loads(line) #dict
    for e in b.keys():
        print("key:",e,"values:",b[e])
