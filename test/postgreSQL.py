#%%
#-*-coding:utf-8
import psycopg2
import sqlalchemy
import pandas as pd

'''
psycopg2를 이용한 db연결은 기존에 내가 사용하던 방법이다. 실행하고자 하는 쿼리를 스트링형태로 그대로 넘겨주면 되서 편하다. 
다만 쿼리 실행 결과가 python list 형태로 반환되는데 이를 다루기가 까다롭다. 그리고 결과만 나오는것도 아쉽다.

예를 들어 select id from users라고 했으면 column name인 ‘id’에 대한 정보까지 따라왔으면 한다. 이를 pandas를 통해 해결할 수 있다. 
pd.read_sql("select id from users limit 1", product)를 실행해보면 column name을 포함하면서도 깔끔하게 쿼리결과를 조회할 수 있다.

'''



# sqlalchemy 연결
def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    #meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con#, meta


# psycopg2 아래 정보를 입력
user = 'puser'
password = '1234'
host_product = 'localhost'
dbname = 'postgres'
port='5432'

product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                            .format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)   

#%% 
try:
    product = psycopg2.connect(product_connection_string)
except:
    print("I am unable to connect to the database")

pc = product.cursor()
pc.execute(query)
pc.fetchall()
#%% 

# psycopg2 쿼리 입력
query = """
select question from question limit 1
"""
# psycopg2 일반적인 쿼리 조회 방법
psycopg2_result = execute(query)



#%%
# psycopg2 pandas를 통한 조회 방법
psycopg2_result2 = pd.read_sql("select id from users limit 1", product)
print(psycopg2_result2)



# sqlalchemy 연결
engine = connect('root_i', '1234', 'postgres')

# sqlalchemy 쿼리 조회
sqlalchemy_result = pd.read_sql("select * from users limit 1", engine)
print(sqlalchemy_result)


'''
2번 방식을 추천하는 이유는 - pandas의 read_sql의 경우 psycopg2로 연결하나 sqlalchemy로 연결하나 상관없음. 
- 다만 read_sql_table의 경우 sqlalchemy연결일때만 동작함. 
- 아래 코드에서 db부분을 psycopg2_connection와 sqlalchemy_connection로 바꿔가며 실행해 보자.
'''

psycopg2_connection = psycopg2.connect(product_connection_string)
sqlalchemy_connection = connect('user 입력', 'password 입력', 'db name 입력')

#db = psycopg2_connection
#db = sqlalchemy_connection

pd.read_sql_query("select id from users limit 1", db)
pd.read_sql("select id from users limit 1", db)
pd.read_sql_table("users", db)