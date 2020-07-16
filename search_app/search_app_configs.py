import os
import pandas as pd

class Config:
    APP_NAME = 'search_app'

class PathConfig(Config):
    temp_path = os.path.dirname(os.path.realpath(__file__))
    current_path = temp_path.replace("\\",'/')

    # 아마도 이게 실질적으로 사용할 path임. 뒤에 파일명만 붙여주면 됨
    DOCUMENT_DATA_PATH = current_path + "/doc_data/"
    RESULT_DATA_PATH = current_path + "/result/"
    
    # doc_data 내부 Directory
    CONTENTSLIST_PATH = DOCUMENT_DATA_PATH + "contentslist/"
    DICTIONARY_PATH = DOCUMENT_DATA_PATH + "dictionary/"
    FASTTEXT_PATH = DOCUMENT_DATA_PATH + "fasttext/"

    MANUAL_PATH = DOCUMENT_DATA_PATH + "manual/"
    MODEL_PATH = DOCUMENT_DATA_PATH + "model/"
    QnA_PATH = DOCUMENT_DATA_PATH + "qna/"
    

class IntentConfigs(Config):
    encode_length = 15
    filter_sizes = [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2]
    num_filters = len(filter_sizes)
    learning_step = 3001
    learning_rate = 0.00001
    vector_size = 300
    fallback_score = 2
    train_fasttext = False
    tokenizing = True

    def __init__(self):
        path = PathConfig()
        self.df = pd.read_excel(path.QnA_PATH, encoding='utf-8')

        intent_list = self.df['Service_Type'].tolist()
        self.intent_mapping = {}

        idx = -1
        for i in intent_list:
            if i not in self.intent_mapping:
                #print(i)
                idx += 1 
                self.intent_mapping[i] = idx
            else:
                pass
        self.label_size = len(self.intent_mapping)
