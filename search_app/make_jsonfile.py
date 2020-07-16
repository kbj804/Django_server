#-*- coding:utf-8 -*-
from docx2python import docx2python
import pandas as pd 
import re
import json
from collections import OrderedDict
from make_dic import generate_Dictionary
from search_app_configs import PathConfig


def remove_blank(text_array):
    texts = []
    for line in text_array:
        #This will ignore empty/blank lines. 
        if line != '':
            # replace \t
            line = line.replace("\t","")
            #Append to list
            texts.append(line)
    return texts

# doc파일을 List로 변환해서 읽기 쉽도록 해줌
def generate_doc(doc_body, doc_len, index_dictionary):  
    for i in range(doc_len):
        # 일반 텍스트 글들 -> 전처리 필요함
        contents_lists = remove_blank(list(doc_body[i][0]))
        temp_list =[]
        last_list_value = contents_lists[-1]
        result_list = []

        # title 이름 저장
        
        # 사전(목차)에 있는 단어인지 비교 후 처리
        for content in contents_lists:
            if content in index_dictionary:
                if temp_list:
                    # 파이썬 list append 함수는 해당 list의 주소를 참조하는 것 이기 때문에 복사 후 넣어줘야함 개고생
                    temp_list2=temp_list[:]
                    result_list.append(temp_list2)
                temp_list.clear()
                temp_list.append(content)


            elif content == last_list_value:
                # 배열 마지막 값 나오면
                temp_list.append(content)
                temp_list2=temp_list[:]
                result_list.append(temp_list2)
                #print(temp_list)
                temp_list.clear()
            else:
                temp_list.append(content)
        return result_list
                    
def make_table_dic(table_list):
    tables = OrderedDict()
    #table_data = OrderedDict()

    for lists in table_list:
        tables[lists[0]]=lists[1]
    #table_dic = dict(zip(*[alist,blist]))
    
    return tables

def generate_table(doc_body, doc_len):
    # 테이블 처리
    table_list=[]
    
    for i in range(doc_len):
        filed_list=[]
        for k in range(len(doc_body[i])):
            filed_list.append(doc_body[i][k][0])
        table_list.append(filed_list)
    #table_dic = make_table_dic(table_list)

    return table_list




# doc파일 내용을 List로 받아서 Json으로 변환
def generate_doc_to_json(index_len, contents_list, main_title, sub_title, title, data_type):
    json_data = OrderedDict()
    #contents_data = OrderedDict()

    content_list=[]
    
    for text in contents_list:
        json_data["data_type"] = data_type
        if index_len == 1:
            json_data["main_title"] = main_title
            json_data["sub_title"] = sub_title
            json_data["title"] = title
        elif index_len ==2 :
            json_data["main_title"] = main_title
            json_data["sub_title"] = sub_title 
            json_data["title"] = title
        elif index_len ==3 :
            json_data["main_title"] = main_title
            json_data["sub_title"] = sub_title
            json_data["title"] = title
        
        content_list.append(text)
        json_data["content"] = content_list
        
    #return json.dumps(json_data, ensure_ascii=False, indent="\t")
    return json_data


def make_jsonFile(dic_path, doc_path, file_name):
    igate_cl = generate_Dictionary(dic_path)
    
    # 목차를 이용하여 사전 생성
    index_dictionary = igate_cl.DICTIONRAY_LIST

    json_file = []
    # 문서 로드 
    doc_result = docx2python(doc_path)
    main_title =''
    sub_title =''
    title=''
    index_len=''

    for j in range(1, len(doc_result.body)):
        doc_body = doc_result.body[j]
        doc_len = len(doc_body)

        
        if doc_len == 1:
            # 문서 스플릿
            doc_list = generate_doc(doc_body, doc_len, index_dictionary)
            print(doc_list)
            for _, content in enumerate(doc_list):
                #print(content)
                for text in content:
                    if text in index_dictionary:
                        #print(text)
                        index = index_dictionary[text] # index는 해당 목차(사전)의 번호
                        index_len = len(index) 
                        
                        # 1: 대분류 / 2: 중분류 / 3: 소분류
                        if index_len == 1: 
                            main_title = text
                            sub_title = text
                            title = text

                        elif index_len ==2 :
                            sub_title = text
                            title = text

                        elif index_len ==3 :
                            title = text
                json_data = generate_doc_to_json(index_len, content, main_title, sub_title, title, "string")
                json_file.append(json_data)
                

        else:
            print('ID = {0}'.format(str(j)))
            # 테이블
            table = generate_table(doc_body, doc_len)
            #print(table)
            json_data= generate_doc_to_json(index_len, table, main_title, sub_title, title, "table")
            json_file.append(json_data)
    
    with open(path.RESULT_DATA_PATH + file_name + '.json', 'w',encoding='utf-8') as make_file:
        json.dump(json_file, make_file,ensure_ascii=False, indent="\t")

if __name__ == "__main__":
    
    path = PathConfig()

    file_name = 'iGate Introduction'

    contentsList_path = path.CONTENTSLIST_PATH + file_name + '_cl.docx'
    manual_doc_path = path.MANUAL_PATH + file_name + '.docx'

    make_jsonFile(contentsList_path, manual_doc_path, file_name)

