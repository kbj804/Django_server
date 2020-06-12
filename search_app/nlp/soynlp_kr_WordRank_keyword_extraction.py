# -*- coding: utf-8 -*-
from krwordrank.word import KRWordRank
import json
from docx2python import docx2python
import numpy as np
from krwordrank.word import summarize_with_keywords

min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)


def json_2_list_Contents(json_path):
    temp_list=[]
    with open(json_path, 'r',encoding='UTF8') as data_file:
        json_data = json.load(data_file)
        for w in json_data:
            if (str(type(w['content'][0])) == "<class 'list'>"):
                # print(type(w['content'][0]))
                # print(w['content'])
                for wl in w['content']:
                    temp_list.extend(wl)
                # temp = np.array(w['content']).flatten().tolist()
                # temp_list.extend(temp)

            else:
                # print(type(w['content'][0]))
                # print(w['content'])
                temp_list.extend(w['content'])
        return temp_list
    

json_path = './server_project/search_app/result/iGate Introduction.json'
contents_list = json_2_list_Contents(json_path)

stopwords = {'Service', '처리', '[그림', '있다.','ID','다양한'}


beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10
#keywords, rank, graph = wordrank_extractor.extract(temp_list, beta, max_iter)
#passwords = {word:score for word, score in sorted(keywords.items(), key=lambda x:-x[1])[:300] if not (word in stopwords)}


keywords = summarize_with_keywords(contents_list, min_count=5, max_length=10, beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)
print(keywords)
# for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
#    print('%8s:\t%.4f' % (word, r))
