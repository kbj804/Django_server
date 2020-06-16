# 목차(Contents List)를 Dictionary로 바꿀 때 사용
# 기본적으로 소문자로 변환해서 사전에 추가하고 그럼
from kiwipiepy import Kiwi
from make_dic import make_dictionary_list
from nlp.kiwi_morp import kiwi_dictionary_n_fuction
import time
import json
import pandas as pd
import os
from configs import configs

class IOHandler:
    """
    handle = IOHandler('test.txt', 'result.txt')
    kiwi.analyze(handle.read, handle.write)
    """
    def __init__(self, input, output):
        self.input = open(input, encoding='utf-8')
        self.output = open(output, 'w', encoding='utf-8')

    def read(self, sent_id):
        if sent_id == 0:
            self.input.seek(0)
            self.iter = iter(self.input)
        try:
            return next(self.iter)
        except StopIteration:
            return None

    def write(self, sent_id, res):
        print('Analyzed %dth row' % sent_id)
        self.output.write(' '.join(map(lambda x:x[0]+'/'+x[1], res[0][0])) + '\n')

    def __del__(self):
        self.input.close()
        self.output.close()



def add_Dictionary(path, contents_list, flag):
    """
    리스트(목차) 받아서 사전화 (영어는 소문자로 transform_List_English2Lower 함수)
    flag = a: 이어쓰기 / w: 새로만들어쓰기 / r: 읽기
    """
    c_list = transform_List_English2Lower(contents_list)

    with open(path, flag, encoding='utf8') as f:
        # kiwi.add_user_word(word, 'NNP', 3.0)
        for word in c_list:
            data = '\n' + word + '\t' + 'NNP' + '\t' + '3.0'
            f.write(data)


# 원본(사용안함)
def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count+=1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count+=1
    return "k" if k_count>1 else "e"


# 문장에 영어 있으면 소문자로 변환
def transform_Sentence_English2Lower(input_s):
    sentence = ""
    s_list=[]
    for word in input_s:
        if  ord('a') <= ord(word.lower()) <= ord('z'):
            s_list.append(word.lower())
        else:
            s_list.append(word)
    return sentence.join(s_list)

# 리스트 받아올때 영어 소문자로 변환 후 반환
def transform_List_English2Lower(input_l):
    contents_list=[]
    for word in input_l:
        contents_list.append(word.lower())
    
    return contents_list


def json_2_list_Contents(json_path):
    """json Data를 다시 List로 변환"""
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
        
        result_list = transform_List_English2Lower(temp_list)
        return result_list

def merge_list(t_list):
    tl=[]
    for l in t_list:
        tl.extend(l)
    return tl


if __name__ == "__main__":
    # 파일 경로

    # 목차 File에서 Contents를 추출하고 사전에 추가할 때 사용 
    """ 
    contents_list = make_dictionary_list(contents_list_path, 0)
    add_Dictionary(dic_path, contents_list, 'a')
    """
    path = configs()
    kiwi_f = kiwi_dictionary_n_fuction(path.dictionary_path())

    # 테스트 용
    # sentence = 'iManager Architecture 지정변경법 가르쳐주세요.'
    # sen = transform_Sentence_English2Lower(sentence)  
    # result = kiwi_f.get_nn(sen)

    # json 파일 리스트로 받아옴
    contents_list = json_2_list_Contents(path.Json_path())

    df = pd.DataFrame({'sentence':contents_list})
    df = df.dropna()

    df["nn_token"] = df['sentence'].apply(lambda x: kiwi_f.get_nn_list(x))
    print(merge_list(df["nn_token"].tolist()))


