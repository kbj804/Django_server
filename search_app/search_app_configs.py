import os

class Config:
    APP_NAME = 'search_app'

class PathConfig(Config):
    current_path = os.path.dirname(os.path.realpath(__file__))

    DICTIONARY_PATH = current_path + "\\doc_data\\new_dict.txt"
    CONTENTSLIST_PATH = current_path + "\\doc_data\\iGate_Contents_list.docx"
    JSON_PATH = current_path + "\\result\\iGate Introduction.json"
    MANUAL_PATH = current_path + "\\doc_data\\iGate Introduction.docx"