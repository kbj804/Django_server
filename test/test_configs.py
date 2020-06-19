import os

class Config:
    APP_NAME = 'test_app'

class PathConfig(Config):
    current_path = os.path.dirname(os.path.realpath(__file__))
    
    # 아마도 이게 실질적으로 사용할 path임. 뒤에 파일명만 붙여주면 됨
    KOREA_ELECT_PATH = current_path + "\\korea_elect\\"
    KAKAO_REG_PATH = current_path + "\\kakao_reg\\"
    OWNER_PROJECT_PATH = current_path + "\\owner_project\\"
    UTILL_FUCTION_PATH = current_path + "\\utill_function\\"


class QueryConfig(Config):
    # insert_elect_data에 사용되는 쿼리
    INSERT_QUESTION_SQL = "insert into qna_db.question (question, intent, sub_intent, q_morp, q_nn, q_vv, date ,answer_id) values(%s, %s, %s, %s, %s, %s, %s, %s)"
    INSERT_ANSWER_SQL = "insert into qna_db.answer (answer, intent, sub_intent, date) values(%s, %s, %s, %s) returning answer_id"


class Database_Info(Config):
    DB_CONFIG = { 
        'host' : 'localhost',
        'user' : 'postgres',
        'password' : '1234',
        'dbname' : 'postgres',
        'port' : '5432'
    }


