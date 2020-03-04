#-*-coding:utf-8
# PostgreSQL에 데이터 Insert 함

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# import os
#print(os.getcwd())

insert_question_sql = "insert into qna_db.question (question, intent, sub_intent, q_morp, q_nn) values(%s, %s, %s, %s, %s) returning question_id"
insert_answer_sql = "insert into qna_db.answer (answer, intent, question_id) values(%s, %s, %s)"

# question Table에 질문데이터 삽입. 전처리 된 csv 파일이 필요함
# question Table에 넣으면서 나오는 question_id를 이용하여 answer Table도 함께 넣음
def insert_question_table(df):
    with connection.cursor() as curs:
        """
        0 - question
        1 - intent
        2 - sub_intent
        3 - q_morp
        4 - q_nn
        5 - question_date
        6 - answer_date
        7 - answer
        """
        for i in range(len(df)):
            question = df.loc[i][0]
            intent = df.loc[i][1]
            sub_intent = df.loc[i][2]

            q_morp = df.loc[i][3]
            q_nn = df.loc[i][4]

            answer = df.loc[i][7]

            curs.execute(insert_question_sql,(question, intent, sub_intent, q_morp, q_nn))
            question_id = curs.fetchone() # (1054, ) 형태로 들어옴
            insert_answer_table(answer, intent, question_id)
        connection.commit()
        
def insert_answer_table(answer, intent, question_id):
    with connection.cursor() as curs:
        curs.execute(insert_answer_sql, (answer, intent, question_id))
        



# engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
# df.to_sql('qna_db.question', engine)


if __name__ == "__main__":
    connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='postgres')

    df = pd.read_csv(r'./server_project/test/korea_elect/result/korea_elect_preprocess.csv')
    insert_question_table(df)

    connection.close()

