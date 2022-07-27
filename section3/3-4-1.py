import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 로그인 유저정보
LOGIN_INFO = {
    'user_id': 'psseung712',
    'user_pw': 'forsim712!'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:

    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    # HTML 소스 확인
    # print('login_req',login_req.text)
    # HTTP Header 확인
    # print('login_req',login_req.headers)

    # Response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        #권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('https://bbs.ruliweb.com/community/board/320211')

        #예외 발생
        post_one.raise_for_status()
        #print(post_one.text)

        #BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, 'html.parser')
        
        # print(soup.prettify())

        article = soup.select("td.subject > div > a ")
        #print(article)

        for i in article:
            if i is not None and \
                    i.string is not None:
                print(i.string)
