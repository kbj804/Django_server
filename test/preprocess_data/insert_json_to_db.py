# -*- coding: utf-8 -*-
import json

import psycopg2
from sqlalchemy import create_engine
import pandas as pd

insert_manual_sql = "insert into qna_db.manual (data_type, main_title, sub_title, title, contents) values(%s, %s, %s, %s, %s)"
input_json_path = './server_project/test/preprocess_data/manual_data.json'
# output_path = './server_project/test/preprocess_data/result.csv'

def insert_manual_table(json_data):
    with connection.cursor() as curs:
        for data in json_data:
            data_type = data['data_type']
            main_title= data['main_title']
            sub_title= data['sub_title']
            title = data['title']

            content = data['content']

            curs.execute(insert_manual_sql,(data_type, main_title, sub_title, title, str(content)))
        
        connection.commit()

if __name__ == "__main__":
    connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='postgres')

    with open(input_json_path, encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        insert_manual_table(json_data)

    connection.close()