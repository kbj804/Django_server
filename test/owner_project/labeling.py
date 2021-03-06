# %%
from numpy import dot
from numpy.linalg import norm
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

import pandas_profiling
# pr = df.profile_report()
# pr.to_file('report.html')


# %%
import os
print(os.getcwd())

# %%
df = pd.read_excel(r"./data.xlsx")
df.head(5)

# %%
df.columns

# %%
df = df[['주민번호','주소','상태','가입일자','최종불입일자','총납입회차','최종불입회차','은행','상품금액','총불입액','해약금액','실입금액','기간입금액','기간할인액','잔여금액','조합예수잔액','납입방법','담당자','부서','연체횟수','성별']]

# %%  전처리 함수들

def export_adress(adress):
    result = adress[0:2]
    return result

# print(export_adress('서울시 구로구 개봉동'))

def export_age(idnum):
    age = 120 - (int(idnum[0:2]))
    return age

def transform_status(current_status, flag):
    if current_status == '가입':
        if flag == 0:
            return '만기'
        else:
            return current_status

    elif current_status == '해약':
        if flag == 0:
            return '만기_해약'
        else:
            return current_status

    elif current_status == '미계좌':
        return '해약'

    elif current_status == '보류':
        return '가입'

    elif current_status == '접수':
        return '가입'

    else:
        return current_status

# print(export_age('590318-1000000'))
#print(transform_status('해약', 0 ))

# %%
df
# %%
# df.isnull()['주민번호']
# Null 값 있는 행 제거 (2만개정도 제거됨)

df = df.dropna(how='any')

df['주소'] = df['주소'].apply(lambda x : export_adress(x))
df['나이'] = df['주민번호'].apply(lambda x : export_age(x))
df['상태'] = df.apply(lambda x: transform_status(x['상태'], x['총납입회차'] - x['최종불입회차']), axis=1)

# %%

dfs=df[['주민번호','주소','상태','가입일자','최종불입일자','총납입회차','최종불입회차','은행','상품금액','총불입액','해약금액','납입방법','담당자','부서','연체횟수','성별','나이']]


# %%

pr = dfs.profile_report()
pr.to_file('report.html')

# %%
dfs.to_csv(r"../owner_project/label.csv", index=False)

# %%
dfs2=df[['주소','상태','은행','상품금액','총불입액','해약금액','납입방법','담당자','부서','연체횟수','성별','나이']]



# %%
pr = dfs2.profile_report()
pr.to_file('label_report.html')
dfs2.to_csv(r"./label2.csv", index=False)

# %%
