#%% loading data
from numpy import dot
from numpy.linalg import norm
import numpy as np

import pandas as pd

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.getcwd())


data = pd.read_csv(r'./korea_elect_faq.csv')
data.head(2)

# %% Columns 뭐 있나 확인
data.columns

# %% 필요한 Columns만 추출
df = data[['업무분류명', '등록일', '수정일', '제목', '내용', 'FAQ분류', 'all_token', 'nn_token']]
df

# %% Columns 이름 변경
df.rename(columns={'업무분류명':'intent', '등록일':'question_date', '수정일':'answer_date', '제목':'question', '내용':'answer', 'FAQ분류':'sub_intent', 'all_token':'q_morp', 'nn_token':'q_nn'}, inplace=True)
df.head(5)
# %%
question_table = df[['question','intent','sub_intent','q_morp','q_nn','question_date','answer_date','answer']]
#answer_table = df[['answer','intent',]]

question_table
# %%
question_table.to_csv(r"./result/korea_elect_preprocess.csv", index=False)
#answer_table.to_csv(r"./korea_elect/result/answer_table.csv", index=False)



# %%
