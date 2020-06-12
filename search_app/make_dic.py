from docx2python import docx2python
import pandas as pd 
import re


def inverse_dic(text_array): # 이것도 안씀
    dic = dict(zip(range(len(text_array)), text_array))
    inv_dic = {v: k for k, v in dic.items()}

    return inv_dic


def remove_blank_and_reg(text_array): # 양 끝에 \t 제거
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

def find_num_n_remove_Front(doc_list): # 앞부분에 있는 숫자를 제거하고 index를 생성
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

def find_num_n_remove_Back(doc_list): # 뒷부분에 있는 숫자(페이지)를 제거
    result_list=[]
    for d_list in doc_list:
        for i in range(len(d_list)-1, 0, -1): # 마지막 인자인 -1은 역수
            if d_list[i].isdigit():
                d_list = re.sub(pattern='[0-9]', repl='', count=1, string=d_list)
            else:
                result_list.append(d_list)
                break
    return result_list



def make_dictionary_list(doc_path, flag):
    """
    flag 0 : Contents_list / 1: Index_list / 2: Dictionary_list
    """
    doc_result = docx2python(doc_path)
    doc_body_for_dic = doc_result.body[0][0][0]
    
    pre_data1 = remove_blank_and_reg(doc_body_for_dic)
    pre_data2, index_list = find_num_n_remove_Front(pre_data1)

    contents_list = find_num_n_remove_Back(pre_data2) # 목차 리스트..! -> 키워드로 활용 가능

    # 목차와 index 를 이용하여 사전 생성
    list_dic ={ key:value for key, value in zip(contents_list ,index_list) }

    # flag 0: contents_list / flag 1: index_list / flag 2: dictionary
    if flag == 0: return contents_list
    elif flag == 1: return index_list
    else: # flag == 2
        return list_dic


# if __name__ == "__main__":
    
#     # [ iGate_Contents_list.docx , iTools_Contents_list.docx ] 
#     result_dic = make_dictionary(r"./server_project/search_app/doc_data/iGate_Contents_list.docx", 2)
#     print(result_dic)

#     # 키워드 한번 보자
#     for key in result_dic.keys():
#         print(key, result_dic[key])