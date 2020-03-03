#%% loading data
from numpy import dot
from numpy.linalg import norm
import numpy as np

import pandas as pd
data = pd.read_csv(r"./token.csv")
data.head(2)

data['token'].isnull().sum()
# overview에서 Null 값을 가진 경우에는 값 제거
data['token'] = data['token'].fillna('')

#%% 형태소 분석이 끝난 후의 질문들로 학습 벡터 생성
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['token'])
# overview에 대해서 tf-idf 수행
print(tfidf_matrix.shape)

# %%
from kiwipiepy import Kiwi
kiwi = Kiwi()
kiwi.load_user_dictionary(r'./userDict.txt')
kiwi.prepare()
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

#%% 직접적으로 비교할 문장을 벡터화하여 두 벡터 사이의 코사인유사도를 구함
sen = '누전차단기 수리는 누가해'

srch_vector = tfidf.transform(get_all_token(sen))

# print(srch_vector.shape)

# linear_kernel는 두 벡터의 dot product 임
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(srch_vector, tfidf_matrix).flatten()

# print(cosine_sim)


sim_rank_idx = cosine_sim.argsort()[::-1]
for i in sim_rank_idx:
    if cosine_sim[i] > 0:
        print('{} / score : {}'.format(data['token'][i], cosine_sim[i]))




# %%
