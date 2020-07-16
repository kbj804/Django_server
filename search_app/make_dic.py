from docx2python import docx2python
import pandas as pd 
import re
from search_app_configs import PathConfig

class generate_Dictionary:
    """
    INDEX_LIST, CONTENTS_LIST, DICTIONARY(INDEX,CONTENTS)
    """
    def __init__(self, contentsList_path):
        doc_result = docx2python(contentsList_path)
        doc_body_for_dic = doc_result.body[0][0][0]
        
        pre_data1 = self.remove_blank_and_reg(doc_body_for_dic)
        pre_data2, self.INDEX_LIST = self.find_num_n_remove_Front(pre_data1)
        self.CONTENTS_LIST = self.find_num_n_remove_Back(pre_data2) # 목차 리스트..! -> 키워드로 활용 가능

        # 목차와 index 를 이용하여 사전 생성
        self.DICTIONRAY_LIST = { key:value for key, value in zip(self.CONTENTS_LIST, self.INDEX_LIST) }

    def remove_blank_and_reg(self, text_array): # 양 끝에 \t 제거
        texts = []
        for line in text_array:
            #This will ignore empty/blank lines. 
            if line != '':
                # replace \t
                line = line.replace("\t","")
                #remove_sign = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\<\>`\'…》]', '', line)
                #Append to list
                texts.append(line)
        return texts

    def find_num_n_remove_Front(self, doc_list): # 앞부분에 있는 숫자를 제거하고 index를 생성
        i_list=[]
        index_list=[]
        contents_list=[]
        for d_list in doc_list:
            cnt = 0 # 목차부분의 1.1. 에서 . 을 제거하기 위해 . 개수 세는 용도
            i_list=[]
            for i in range(len(d_list)):
                if d_list[i].isdigit(): # 문자열 맨 앞에 숫자가 있으면 제거
                    cnt += 1
                    i_list.append(d_list[i])
                    d_list = re.sub(pattern='[0-9]', repl='', count=1, string=d_list)

                else: # 숫자 아니면 contents_list에 append해서 할당
                    d_list = d_list.replace(".", "", cnt-1)
                    contents_list.append(d_list)
                    index_list.append(i_list)

                    break
        return contents_list, index_list

    def find_num_n_remove_Back(self, doc_list): # 뒷부분에 있는 숫자(페이지)를 제거
        result_list=[]
        for d_list in doc_list:
            for i in range(len(d_list)-1, 0, -1): # 마지막 인자인 -1은 역수
                if d_list[i].isdigit():
                    d_list = re.sub(pattern='[0-9]', repl='', count=1, string=d_list)
                else:
                    result_list.append(d_list)
                    break
        return result_list



if __name__ == "__main__":
    
    file_name = 'iTools Guide v1.0.1'
    path = PathConfig()
    dictionary = generate_Dictionary(path.CONTENTSLIST_PATH + file_name + '_cl.docx')
    print(dictionary.CONTENTS_LIST)
    print(dictionary.INDEX_LIST)
    print(dictionary.DICTIONRAY_LIST)
