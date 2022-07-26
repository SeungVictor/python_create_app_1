from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/tag-curation/skill/57/"
#quote = rep.quote_plus("추천-강좌")
url = base
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.find("div", class_="tag-courses__list-cover e-tag-courses__list-cover")
a = recommand.select("h3", class_="course-card__title")

for i in range(len(a)):
    print(a[i].text)
