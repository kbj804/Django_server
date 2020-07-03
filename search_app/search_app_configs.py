import os
import pandas as pd

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
    QnA_PATH = DOCUMENT_DATA_PATH + "Manual_QnA_v1.0.xlsx"
    
    # INTENT Learning
    FASTTEXT_DIR = DOCUMENT_DATA_PATH + "fasttext\\"
    model_path = DOCUMENT_DATA_PATH + "model\\"

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
