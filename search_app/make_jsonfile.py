from docx2python import docx2python
import pandas as pd 
import re
import json
from collections import OrderedDict
from make_dic import make_dictionary



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




def make_jsonFile():
    # 목차를 이용하여 사전 생성
    index_dictionary = make_dictionary(r"./server_project/search_app/doc_data/iXVDR_CL.docx", 2)
    json_file = []
    # 문서 로드 
    doc_result = docx2python(r"./server_project/search_app/doc_data/iXVDR_Manual_양식.docx")
    main_title =''
    sub_title =''
    title=''
    index_len=''

    for j in range(1,len(doc_result.body)):
        doc_body = doc_result.body[j]
        doc_len = len(doc_body)

        
        if doc_len == 1:
            # 문서 스플릿
            doc_list = generate_doc(doc_body, doc_len,index_dictionary)
            for i, content in enumerate(doc_list):
                print(content)
                for text in content:
                    if text in index_dictionary:
                        print(text)
                        index = index_dictionary[text]
                        index_len = len(index)
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
    
    with open(r"./server_project/search_app/result/iXVDR_Sample.json",'w',encoding='utf-8') as make_file:
        json.dump(json_file, make_file,ensure_ascii=False, indent="\t")

make_jsonFile()