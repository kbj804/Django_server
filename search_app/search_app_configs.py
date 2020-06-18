import os

class Config:
    APP_NAME = 'search_app'

class PathConfig(Config):
    current_path = os.path.dirname(os.path.realpath(__file__))
    
    # 아마도 이게 실질적으로 사용할 path임. 뒤에 파일명만 붙여주면 됨
    DOCUMENT_DATA_PATH = current_path + "\\doc_data\\"
    RESULT_DATA_PATH = current_path + "\\result\\"

    # Sample Test용
    DICTIONARY_PATH = DOCUMENT_DATA_PATH + "new_dict.txt"
    CONTENTSLIST_PATH = DOCUMENT_DATA_PATH + "iGate_Contents_list.docx"
    JSON_PATH = RESULT_DATA_PATH + "iGate Introduction.json"
    MANUAL_PATH = DOCUMENT_DATA_PATH + "iGate Introduction.docx"