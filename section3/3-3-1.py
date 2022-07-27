import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# r = requests.get('https://api.github.com/events')
# #r.raise_for_status() #에러가발생했을때 예외를 던지는 함수
# #print(r.text)

jar = requests.cookies.RequestsCookieJar() #cookie jar를 생성
jar.set('name','kim',domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com',timeout=3)
# print(r.text)

# r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
# print(r.text)


payload1 = {'key1': 'value1', 'key2': 'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple 둘다 결과같음
payload3 = {'some':'nice'}

r = requests.post('http://httpbin.org/post', data=payload1) #form
print(r.text)

r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) #json으로보낼때는 json.dumps를 사용
print(r.text)
