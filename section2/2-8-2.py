from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="./imagedown_inf"
url = "https://www.inflearn.com/tag-curation/skill/57/"
#quote = rep.quote_plus("추천-강좌")
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.find("div", class_="tag-courses__list-cover e-tag-courses__list-cover")
a = recommand.select("img", alt="image")
b = recommand.select("h3", class_="course-card__title")


try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

try:
    for i,e in enumerate(a,1):
        with open(savePath+ "title_"+str(i)+".txt", "wt") as f:
            f.write(b[i-1].text)
            fullfilename = os.path.join(savePath,savePath+'img_'+str(i)+'.png')
            time.sleep(0.5)
            req.urlretrieve(e['src'],fullfilename)
except:
    print("Error")
    pass

print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")


