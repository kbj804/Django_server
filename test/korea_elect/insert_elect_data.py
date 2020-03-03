#-*-coding:utf-8
# PostgreSQL에 데이터 Insert 함

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# import os
# print(os.getcwd())

insert_question_sql = "insert into qna_db.question (question, intent, sub_intent, q_morp, q_nn) values(%s, %s, %s, %s, %s)"

def insert_question_table():
    with connection.cursor() as curs:
        """
        0 - question
        1 - intent
        2 - sub_intent
        3 - q_morp
        4 - q_nn
        """
        for i in range(len(df)):
            question = df.loc[i][0]
            intent = df.loc[i][1]
            sub_intent = df.loc[i][2]

            q_morp = df.loc[i][3]
            q_nn = df.loc[i][4]

            curs.execute(insert_question_sql,(question, intent, sub_intent, q_morp, q_nn))
        connection.commit()
        

# engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
# df.to_sql('qna_db.question', engine)

print(len(df))
print(len(df.columns))

if if __name__ == "__main__":
    connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='postgres')

    df = pd.read_csv(r'./server_project/test/korea_elect/result/question_table.csv')
    insert_question_table()

    connection.close()

