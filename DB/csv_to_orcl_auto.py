!python -m pip install oracledb --upgrade

import oracledb as od
import pandas as pd
import os

#오라클연결
conn = od.connect(user='c##doy0202',
          password='c##doy0202',
          dsn="127.0.0.1:1521/orcl") #본인 계정으로 로그인

#커서
cursor = conn.cursor()

#테이블 생성
cursor.execute("create table dy4("+ #csv파일을 반영할 table 생성
              "mname varchar2(30) ," +
              "time varchar2(30),"+
              "xmin number(8,4) ," +
              "ymin number(8,4) ,"+
              "xmax number(8,4) ,"+
              "ymax number(8,4) ,"+
              "confidence number(8,4) ,"+
              "class int"
              ")")
cursor.close()
conn.close()


# 파일 경로
fl = os.listdir('C:/KFQ_BigData/Final_Proj/KFQ_TEAM01-2/yolo/results/xlsxdata') #csv 파일 들어있는 폴더로 경로 지정
print(fl) #폴더 안의 파일들 list로 불러오기

os.path.join('C:/KFQ_BigData/Final_Proj/KFQ_TEAM01-2/yolo/results/xlsxdata/',fl[0]) #첫번째 파일명 확인/ 아마 첫 파일이 DS_Store면 밑에 포문 안되는 듯..

conn = od.connect(user='c##doy0202', #본인 계정으로 바꾸기
          password='c##doy0202',
          dsn="127.0.0.1:1521/orcl")
cursor = conn.cursor()
for fn in fl:
    df = pd.read_csv(os.path.join('C:/KFQ_BigData/Final_Proj/KFQ_TEAM01-2/yolo/results/xlsxdata/',fn)) #폴더+파일명
    for i,row in df.iterrows():
        cursor.execute("insert into dy4 "+ #만든 테이블명으로 바꾸기
              "values(:mname, :time, :xmin, :ymin, :xmax, :ymax, :confidence, :class) ",
              [row['name'],row['time'],row['xmin'],row['ymin'],row['xmax'],row['ymax'],row['confidence'],row['class']])
conn.commit()
cursor.close()
conn.close()

#오라클에 연결해서 테이블 불러오기(확인)
conn = od.connect(user='c##doy0202', #본인 계정으로 바꾸기
          password='c##doy0202',
          dsn="127.0.0.1:1521/orcl")
cursor = conn.cursor()
cursor.execute("select * from dy4") #만든 테이블명으로 바꾸기
rows = cursor.fetchall()
colname = cursor.description
cursor.close()
conn.close()
cns = [cn[0] for cn in colname]
df = pd.DataFrame(rows,columns=cns)
df