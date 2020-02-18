#-*-coding:utf-8
import psycopg2
import pandas as pd

def execute(query):
    pc.execute(query)
    return pc.fetchall()


#아래 정보를 입력
user = 'root_i'
password = '1234'
host_product = 'localhost'
dbname = 'postgres'
port='2345'

product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                            .format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)    
try:
    product = psycopg2.connect(product_connection_string)
except:
    print("I am unable to connect to the database")

pc = product.cursor()


#쿼리 입력
query = """
select id from users limit 1
"""

#일반적인 쿼리 조회 방법
result = execute(query)

#pandas를 통한 조회 방법
result2 = pd.read_sql("select id from users limit 1", product)
print(result2)