# -*- coding: utf-8 -*-
from krwordrank.word import KRWordRank
import json
from docx2python import docx2python
import numpy as np
from krwordrank.word import summarize_with_keywords

min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)


json_path = './server_project/search_app/result/iGate Introduction.json'

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
    
    


# doc_path = "./server_project/search_app/doc_data/iGate Introduction.docx"
# doc_result = docx2python(doc_path)
# print(doc_result.body)

# texts = ['iGate란', 'iGate 4.0 는 SOA(Service-Oriented Architecture)기반의 ESB 엔진을 근간으로 하고 있으며, 대/내외의 채널별 공통 업무와 채널 고유 업무를 효율적으로 처리하는 중요 영역과 Application 의 인터페이스 표준화를 지원함으로써 Middle Layer Integration 의 실현을 위해 다음과 같은 사상을 기본으로 하는 솔루션이다.', '서비스 통합', '--기존의 각 어플리케이션들은 멀티채널  통합 아키텍처 상에서 통합되어야 한다.', '--코어의 어플리케이션들은 SOA 상에서 데이터 로직을 제공하는 서비스 프로바이더로 존재하고, 비즈니스 프로세스는 멀티채널 통합 layer에 구현된다. 이러한 비즈니스 프로세스는 각  채널에서 재사용, 공유하여야 한다.', '재사용성 극대화', '--프레젠테이션 로직과 비즈니스 로직을 분리하여 구현되어야 한다.', '--특정 기능을 수행하는 비즈니스 로직은 전사적으로 하나만 존재하며, 프레젠테이션 로직은 채널 및 사용자 특성별로 다양하게 구성할 수 있어야 한다.', '메시지 및 인터페이스 표준화', '--전사적인 표준 메시지를 통한 Integration Tier의 일관성 있는 비즈니스를 지원한다 ', '--ESB를 기반으로 인터페이스를 표준화한다.', '고가용성 확보', '--iGate를 통해 제공되는 모든 서비스는 24x365 운영을 고려하여 설계 및 구현한다.', '--대용량 세션 및 거래를 처리할 수 있는 안정성이 검증된 아키텍처로 구현한다.']

beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10

print(temp_list)

stopwords = {'Service', '처리', '[그림', '있다.','ID','다양한'}

#keywords, rank, graph = wordrank_extractor.extract(temp_list, beta, max_iter)
#passwords = {word:score for word, score in sorted(keywords.items(), key=lambda x:-x[1])[:300] if not (word in stopwords)}

keywords = summarize_with_keywords(temp_list, min_count=5, max_length=10, beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)
print(keywords)
# for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
#    print('%8s:\t%.4f' % (word, r))
