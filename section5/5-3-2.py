import sqlite3
import simplejson as json
import datetime

#DB생성(파일)
conn = sqlite3.connect('./section5/databases/sqlite.db', isolation_level=None)
#날짜 생성
now = datetime.datetime.now()
print('now',now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)
#커서 바인딩
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)") #AUTOINCREMENT 도 가능 #INTERGER대문자
with open('./section5/data/users.json','r') as infile:
    r = json.load(infile)
    for user in r:
        c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
        (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime))
        

#데이터 조회(전체)
c.execute("SELECT * FROM users")

#1개 로우 선택
print(c.fetchone())

#지정 로우 선택
print(c.fetchmany(size=3))

#전체 로우 선택
print(c.fetchall()) #cursor에 있는 데이터를 모두 읽어옴

#순회1
rows = c.fetchall()
for row in rows:
    print('usage1 >',row)

#순회2
for row in c.fetchall():
    print('usage2 >',row)

#순회3 내림차순(execute로바로 실행 )
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('usage3 > ',row)

#조건 조회1
param1 = (1,) #tuple로받음 리스트로 넣어도됨
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1',c.fetchone())
print('param1',c.fetchall())

#조건 조회2(python 문자열 맵핑)
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2) #%s %d %f %o
print('param2',c.fetchone())
print('param2',c.fetchall())

#조건 조회3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3',c.fetchone())
print('param3',c.fetchall())

#조건 조회4
param4 = (1,4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4',c.fetchall())

#조건 조회5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5',c.fetchall())

#조건 조회6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6',c.fetchall())

#dump (쿼리문 로그같은것?)
with conn:
    #Dump 출력
    with open('./section5/data/test.dump', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')
