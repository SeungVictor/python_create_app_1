from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <h1>Find VS Select 차이</h1>
  <p>CSS 선택자를 사용 및 다중반환</p>
  <p>태그선택자 사용 및 단일반환</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print('prettyfy', soup.prettify())

h1 = soup.html.body.h1
print('h1',h1)
print("------------------------------")

p1 = soup.html.body.p
print('p1',p1)
print("------------------------------")
p2 = p1.next_sibling.next_sibling #줄바꿈때문에 두번넣어야함 
print('p2',p2)
print("------------------------------")
p3 = p1.previous_sibling.previous_sibling
print('p3',p3)
print("------------------------------")
print("h1 = " + h1.string)
print("------------------------------")
print("p  = " + p1.string)
print("------------------------------")
print("p  = " + p2.string)
