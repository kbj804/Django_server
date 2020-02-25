from django.test import TestCase

# Create your tests here.

#-*- coding:utf-8 -*-
import requests
import json
import ast

import urllib3

#from chat.consumers import ChatConsumer


accessKey = "aac4fba1-db31-4078-96d9-f21671d9ed9b"
url = 'http://localhost:8000/search_app/?'

def extract_keyword(user_message):
    openApi_NLU_URL = "http://aiopen.etri.re.kr:8000/WiseNLU"
    analysisCode = "ner"

    text = user_message

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text": text,
            "analysis_code": analysisCode
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApi_NLU_URL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    p = str(response.data,"utf-8")
    d = ast.literal_eval(p)
    #print(d)

    # 명사 2개 이상인건 붙여서 검색해야 함
    word=''
    for i in d['return_object']['sentence'][0]['morp']:
        if i['type'] in ['NNG','NNP','NNB','SL']:
            word += i['lemma']
            word += ' '
    print("WORD : ", word)

    return word


    

# 임시 데모를 위해 table타입 없애고 String만 추출함
def return_string(es_result):
    try:
        for i in range(0,int(es_result['total'])-1):
            data_type = es_result['hits'][i]['_source']['data_type']
            if data_type == 'string':
                print(json.dumps(es_result, indent=4,  ensure_ascii=False))
                return es_result['hits'][i]['_source']['content']
            else:
                print("ERROR: NOT EXIST STRING TYPE")

    
    except:
        return list('모르겠어요')




def search_elastic(word):
    try:
        method = 'search_content'
        query = url + method + '=' + word
        res = requests.get(query)
        #print(res.text)
        # ast => String 타입을 Dic 으로 변환
        es_result = ast.literal_eval(res.text)
        #print(json.dumps(es_result, indent=4,  ensure_ascii=False))
        return es_result

    except:
        print("### search_elastic ERROR ###")
        return res.text


# 임시 상위 스코어 ELK 검색결과 리턴 
def request_message(user_message):

    openApi_MR_URL = "http://aiopen.etri.re.kr:8000/MRCServlet"
    

    word = extract_keyword(user_message)
    es_result = search_elastic(word)

    #print(json.dumps(docs, indent=4,  ensure_ascii=False)) # json 파일 이쁘게 출력
 
    messages = return_string(es_result)
    #print(messages)
    passage = ' '.join(messages)
    print("Passage : ",passage)
    question = user_message

    requestJson = {
    "access_key": accessKey,
        "argument": {
            "question": question,
            "passage": passage
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApi_MR_URL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    
    p = str(response.data,"utf-8")
    d = ast.literal_eval(p)
    #print(d)
    message = d['return_object']['MRCInfo']['answer']
    
    return message

    # if method == 'search_content':
    #     string_contents = []
    #     for hit in docs['hits'][0:5]:
    #         #print(hit['_source'])
    #         content = hit['_source']['content']
    #         if hit['_source']['data_type'] == 'table':
    #             for coulm in hit['_source']['content']:
    #                 #print(coulm)
    #                 pass
            
    #         # String - content
    #         else:
    #             for line in content:
    #                 string_contents.append(line)

    #     # 리스트 -> 문자열 
    #     passage = '. '.join(string_contents)





### 
# print("[responseCode] " + str(response.status))
# print("[responBody]")
# print(str(response.data,"utf-8"))
###


""" question = "adapter 설정에 대해 알려줘"

    requestJson = {
    "access_key": accessKey,
        "argument": {
            "question": question,
            "passage": passage
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApi_MR_URL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    print(str(response.data,"utf-8"))
    p = str(response.data,"utf-8")
    d = ast.literal_eval(p)
     
    print(d)
    print(question)
    print(d['return_object']['MRCInfo']['answer'] + '합니다') """


