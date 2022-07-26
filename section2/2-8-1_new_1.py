from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os
from urllib import parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "./imagedown"  # C:\imagedown\

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")


# naver 이미지 검색결과에서 이미지url parser하기 
a = soup.select("#main_pack > script:nth-child(10)")
b = a[0].text
c = b.split(",")
d = [x.strip() for x in c]
e = [x for x in d if x.startswith("\"originalUrl\":")]
f = [x.replace("\"", "") for x in e]
img_list = []
for i in range(len(f)):
    encoded_url =f[i].split(":")[1]
    #parser한 이미지 url decoding하기
    decoded_url = parse.unquote(encoded_url, encoding="utf-8")
    img_list.append(decoded_url)



for i, img_list in enumerate(img_list, 1):
    
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(img_list, fullFileName)

print("다운로드 완료")
