from docx2python import docx2python
import pandas as pd 
import re

def remove_blank_and_reg(text_array):
    texts = []
    for line in text_array:
        #This will ignore empty/blank lines. 
        if line != '':
            # replace \t
            line = line.replace("\t","")
            remove_sign = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\<\>`\'…》]', '', line)
            #Append to list
            texts.append(remove_sign)
    return texts

def reduce_num(text_array):
    texts =[]
    index_list =[]
    for line in text_array:
        i = list(filter(str.isdigit, line))
        # 배열 검사
        if i:
            # 숫자 있는 값만 추출 -> 그리고 페이지가 100페이지(3자리) 이상 가는건 한번 더 pop 해줘야 함...ㅠㅠ 나중에처리
            i.pop()
            i.pop()
            index_list.append(i)
            remove_digit = re.sub('[[\d\]+]', '', line)
            texts.append(remove_digit)
    return texts, index_list
    



def inverse_dic(text_array):
    dic = dict(zip(range(len(text_array)), text_array))
    inv_dic = {v: k for k, v in dic.items()}

    return inv_dic

def make_dictionary():
    doc_result = docx2python(r"./doc_data/contents_list.docx")
    doc_body_for_dic = doc_result.body[0][0][0]
    first = remove_blank_and_reg(doc_body_for_dic)
    contents_list, index_list = reduce_num(first)

    # 목차와 index 를 이용하여 사전 생성
    list_dic ={ key:value for key, value in zip(contents_list ,index_list)}
    #list_dic = inverse_dic(second)
    print(list_dic)
    
    return list_dic
