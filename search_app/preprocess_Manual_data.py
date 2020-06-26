# Manual Feature 추출

import pandas as pd 
import re

from search_app_configs import PathConfig
from nlp.kiwi_morp import kiwi_dictionary_n_fuction


def preprocess_data(tokenizing):
    df['intent'] = df['Service_Type'].map(intent_mapping)
    path = PathConfig()
    kiwi_f = kiwi_dictionary_n_fuction(path.DICTIONARY_PATH)

    if tokenizing:
        count = 0
        for i in df['Question']:
            df.replace(i, kiwi_f.get_token_str(i), regex=True, inplace=True)
            if count % 50 == 0:
                print("CURRENT COLLECT : ", count)
            count += 1

    encode = []
    decode = []
    for q, i in zip(df['Question'],df['Service_Type']):
        encode.append(q)
        decode.append(i)
    # encode: Question, decode: Intent Idx
    return {'encode': encode, 'decode': decode}


if __name__ == "__main__":
    df = pd.read_excel(r"./server_project/search_app/doc_data/Manual_QnA_v1.0.xlsx")
    print(set(df['Service_Type'].tolist()))
    
    intent_list = df['Service_Type'].tolist()
    intent_mapping = {}

    idx = -1
    for i in intent_list:
        if i not in intent_mapping:
            #print(i)
            idx += 1 
            intent_mapping[i] = idx
        else:
            pass
        
    #print(intent_mapping)

    train_data_list = preprocess_data(tokenizing=True)
    #print(train_data_list)