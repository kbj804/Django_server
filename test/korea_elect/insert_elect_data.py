#-*-coding:utf-8
# PostgreSQL에 초기 데이터 Insert 

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# import os
#print(os.getcwd())

insert_question_sql = "insert into qna_db.question (question, intent, sub_intent, q_morp, q_nn, q_vv, date ,answer_id) values(%s, %s, %s, %s, %s, %s, %s, %s)"
insert_answer_sql = "insert into qna_db.answer (answer, intent, sub_intent, date) values(%s, %s, %s, %s) returning answer_id"

# question Table에 질문데이터 삽입. 전처리 된 csv 파일이 필요함
# question Table에 넣으면서 나오는 question_id를 이용하여 answer Table도 함께 넣음
def insert_table(df):
    with connection.cursor() as curs:
        """
        0 - question
        1 - intent
        2 - sub_intent
        3 - q_morp
        4 - q_nn
        5 - q_vv
        6 - question_date
        7 - answer_date
        8 - answer
        """
        for i in range(len(df)):
            question = df.loc[i][0]
            intent = df.loc[i][1]
            sub_intent = df.loc[i][2]

            q_morp = df.loc[i][3]
            q_nn = df.loc[i][4]
            q_vv = df.loc[i][5]

            q_date = df.loc[i][6]
            a_date = df.loc[i][7]

            answer = df.loc[i][8]

            # Answer Table 에 데이터를 넣고 answer_id를 리턴 받음
            curs.execute(insert_answer_sql, (answer, intent, sub_intent, str(a_date)))
            answer_id = curs.fetchone() # (1054, ) 형태로 들어옴

            # 리턴받은 answer_id를 이용하여 question Table 에 나머지 데이터를 삽입.
            curs.execute(insert_question_sql, (question, intent, sub_intent, q_morp, q_nn, q_vv, str(q_date), answer_id))


        connection.commit()
        

        



# engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
# df.to_sql('qna_db.question', engine)


if __name__ == "__main__":
    try:
        connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='postgres')

        df = pd.read_csv(r'./server_project/test/korea_elect/result/korea_elect_preprocess.csv')
        insert_table(df)

        connection.close()

    except Exception as e:
        print(e)
        connection.close()
