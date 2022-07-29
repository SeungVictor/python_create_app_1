import FinanceDataReader as fdr
import pandas as pd
import datetime
import sqlite3

#pandas, pandas_datareader 설치

try:
    with sqlite3.connect('./section5/databases/sqlite_new.db') as conn: #DB생성(파일)

        #조회 시작 & 마감 날짜
        start = datetime.datetime(2022,2,4)
        end = datetime.datetime(2022,2,25)

        gs = fdr.DataReader('090430', start, end) #아모레퍼시픽 주가 읽기

        #데이터 출력
        print(gs)

        #인덱스 출력
        print(gs.index)

        #Column 출력
        print(gs['Open'])

        #Row 출력
        print(gs.loc['2022-02-14'])

        #상세 정보
        print(gs.describe())

        #Index To Column1
        gs['Date'] = gs.index

        #인덱스 재 설정
        gs.index = range(1,(len(gs.index)+1))

        #데이터 출력(확인)
        print(gs)

        #pandas to DataBase(to_sql) ORM기능
        # conn <- cursor가져오는것
        # replace는 이미 있는 테이블을 삭제하고 새로 생성하는 기능
        # fail 테이블이 있으면 실패처리함(한번만실행됨)
        # fail 놓고 append로 추가하면서 실행해야 데이터 안없어짐 
        # index true로 하고 id로지정하면 알아서넣어줌
        # index false로하면 index생성안함 
        gs.to_sql("TEST", conn, if_exists="replace", index=True, index_label='Id') #fail, replace, append

        #커밋
        conn.commit()

        #pandas read DataBase(read_sql) 전체 조회
        df = pd.read_sql(('select * from "TEST"'), conn) #index_col='Id', columns=['Open', 'High'...]
        print(df)

        #pandas read DataBase(read_sql) 조건 조회
        df = pd.read_sql('select * from "TEST" WHERE Id = ? OR Id = ?', conn, params=(3,7), index_col='Id') #params : list, tuple or dict..
        print(df)

finally:
    print('Dataframe SQL Work complete!')
