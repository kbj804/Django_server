 #-*- coding: utf-8 -*-
 # 1차 전처리
 # 형태소 분리 후 새로운 CSV파일 생성 
import re
import pandas as pd
from kiwipiepy import Kiwi
import sys
import os
# 상위폴더 두번 뒤로가는거
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from search_app.nlp.kiwi_morp import kiwi_dictionary_n_fuction


if __name__ == '__main__':

    elect_kiwi = kiwi_dictionary_n_fuction(r'./server_project/test/korea_elect/korea_elect_userDict.txt')


    raw_data = pd.read_csv(r"./server_project/test/korea_elect/data/KEI_FAQ_data.csv")
    print(raw_data.head())
    raw_data = raw_data.dropna() # null값 있는 행 제거

    # raw_data["token"] = raw_data["제목"].apply(lambda x: get_noun(x))
    # raw_data.to_csv(r"./server_project/test/nn_token.csv", index=False)

    # raw_data["token"] = raw_data["제목"].apply(lambda x: get_all_token(x))
    # raw_data.to_csv(r"./server_project/test/token.csv", index=False)

    raw_data["all_token"] = raw_data["제목"].apply(lambda x: elect_kiwi.get_all_token(x))
    raw_data["nn_token"] = raw_data["제목"].apply(lambda x: elect_kiwi.get_noun(x))
    raw_data["vv_token"] = raw_data["제목"].apply(lambda x: elect_kiwi.get_vv(x))

    # raw_data.to_csv(r"./server_project/test/korea_elect/korea_elect_FAQ.csv", index=False)
