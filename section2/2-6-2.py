#2019-01-28 수정

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("./section2/food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup)

# css선택자 6가지방법
print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li 태그 그룹의 4번째 요소중 2번째
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #1개여도 인덱스로접근
print("4", soup.select("#ac-list > li.alcohol.high")[0].string) #class로접근
#id는 #을 사용해야함 띄어쓰기는 .을 사용해야함

param = {"data-lo": "cn", "class": "alcohol"}
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
