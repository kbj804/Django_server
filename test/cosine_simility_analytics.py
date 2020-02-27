#%% loading data

from numpy import dot
from numpy.linalg import norm
import numpy as np

import pandas as pd
data = pd.read_csv(r'D:/Project/Django/Scripts/server_project/test/movies_metadata.csv', low_memory=False)

data.head(2)


# %%
data['overview'].isnull().sum()

# %%
data['overview'] = data['overview'].fillna('')
# overview에서 Null 값을 가진 경우에는 값 제거

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
# overview에 대해서 tf-idf 수행
print(tfidf_matrix.shape)

#%%
srch_vector = vectorize.transform([
    '공장을 이전하였는데 전기설비를 옮겨서 계속 사용할 수 있나요?'
])

# %% 코사인 유사도를 구합니다.
# linear_kernel는 두 벡터의 dot product 임
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# %% 영화의 타이틀과 인덱스를 가진 테이블을 만듭니다
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print(indices.head())

# %%
def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아옵니다. 이제 선택한 영화를 가지고 연산할 수 있습니다.
    idx = indices[title]

    # 모든 영화에 대해서 해당 영화와의 유사도를 구합니다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 영화들을 정렬합니다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화를 받아옵니다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 영화의 인덱스를 받아옵니다.
    movie_indices = [i[0] for i in sim_scores]

    # 가장 유사한 10개의 영화의 제목을 리턴합니다.
    return data['title'].iloc[movie_indices]

# %%
idx = indices['Father of the Bride Part II']
print(idx)

# %%
get_recommendations('Batman Forever')

# %%
sim_scores = list(enumerate(cosine_sim[4]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
sim_scores = sim_scores[0:11]
movie_indices = [i[0] for i in sim_scores]
print(data['title'].iloc[movie_indices])

# %%
