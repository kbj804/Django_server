import pandas as pd
pd.options.mode.chained_assignment = None

import numpy as np
np.random.seed(0)

from konlpy.tag import Twitter
twitter = Twitter()

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

# tokenizer : 문장에서 색인어 추출을 위해 명사,동사,알파벳,숫자 정도의 단어만 뽑아서 normalization, stemming 처리하도록 함
def tokenizer(raw, pos=["Noun","Alpha","Verb","Number"], stopword=[]):
    return [
        word for word, tag in twitter.pos(
            raw, 
            norm=True,   # normalize 그랰ㅋㅋ -> 그래ㅋㅋ
            stem=True    # stemming 바뀌나->바뀌다
            )
            if len(word) > 1 and tag in pos and word not in stopword
        ]

# 테스트 문장
rawdata = [
    '남북 고위급회담 대표단 확정..남북 해빙모드 급물살',
    '[남북 고위급 회담]장차관만 6명..판 커지는 올림픽 회담',
    
    '문재인 대통령과 대통령의 영부인 김정숙여사 내외의 동반 1987 관람 후 인터뷰',
    '1987 본 문 대통령.."그런다고 바뀌나? 함께 하면 바뀐다"',
    
    '이명박 전 대통령과 전 대통령의 부인 김윤옥 여사, 그리고 전 대통령의 아들 이시형씨의 동반 검찰출석이 기대됨'
]
