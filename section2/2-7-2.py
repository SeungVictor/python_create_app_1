# 2019-01-29 수정
# 기존 naver 주식 사이트 : ajax 방식으로 변경으로 인해 이를 반영한 코드를 수정.

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')  # utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐

# 중간 출력
# print(res)

soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#popularItemList > li > a")
top10_price = soup.select("#popularItemList > li > span")
print(top10_price[0].text.strip())

ranking = []
company = []
price = []
for i in range(len(top10)):
    ranking.append(i+1)
    company.append(top10[i].text.strip())
    price.append(top10_price[i].text.strip())
    df = pd.DataFrame({"ranking": ranking, "company": company, "price": price})
print(df)

for i in range(len(top10)):
    print("검색 {0}순위, 회사명 :{1}, 주가 :{2}".format(i+1, top10[i].text.strip(), top10_price[i].text.strip()))
  
    
