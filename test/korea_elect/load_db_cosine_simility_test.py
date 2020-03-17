#-*-coding:utf-8
# PostgreSQL에 초기 데이터 Insert 

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# import os
#print(os.getcwd())



if __name__ == "__main__":
    try:
        connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='postgres')

        # df = pd.read_csv(r'./server_project/test/korea_elect/result/korea_elect_preprocess.csv') 52515071 15442744
        # insert_table(df)
        with connection.cursor() as curs:
            sql = 'select * from qna_db.question where answer_id is null'
            curs.execute(sql)
            result = curs.fetchall()
            print(result)

        connection.commit()
        connection.close()

    except Exception as e:
        print(e)
        connection.close()
