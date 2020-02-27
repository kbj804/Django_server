 #-*- coding: utf-8 -*-
import re
import pandas as pd
from kiwipiepy import Kiwi


def generate_morp_word(sentence,analyze_num):
    try:
        result = kiwi.analyze(sentence, analyze_num)
        print(result)
        morp_word_list =[]
        morp_nn_list=[]
        morp_vv_list=[]

        for i in range(0, analyze_num):
            morp_word = ''
            morp_nn=''
            morp_vv=''
            #print(i)
            for word in result[i][0]:
                morp_word += word[0]
                morp_word += ' '
                if word[1] in ['NNG','NNP','NNB','NP','SL','SN']:
                    morp_nn += word[0]
                    morp_nn += ' '
                elif word[1] in ['VV','VA','VX','VCP','VCN']:
                    morp_vv += word[0]
                    morp_vv += ' '

            morp_word_list.append(morp_word)
            morp_nn_list.append(morp_nn)
            morp_vv_list.append(morp_vv)
        return morp_word_list, morp_nn_list, morp_vv_list
    except:
        print("### ERROR 형태소 분석기 부분 에 뭐가 잘못된게 있는듯 ERROR ### ")


def get_noun(sen):
    morp_list, nn_list, vv_list = generate_morp_word(sen, 1)
    return nn_list

def get_all_token(sen):
    morp_list, nn_list, vv_list = generate_morp_word(sen, 1)
    return morp_list


if __name__ == '__main__':
    kiwi = Kiwi()
    kiwi.load_user_dictionary(r'./server_project/test/userDict.txt')
    kiwi.prepare()


    raw_data = pd.read_csv(r"./server_project/test/한국전력공사_FAQ_data.csv")
    print(raw_data.head())
    raw_data = raw_data.dropna()

    raw_data["token"] = raw_data["제목"].apply(lambda x: get_noun(x))
    raw_data.to_csv(r"./server_project/test/nn_token.csv", index=False)

    raw_data["token"] = raw_data["제목"].apply(lambda x: get_all_token(x))
    raw_data.to_csv(r"./server_project/test/token.csv", index=False)