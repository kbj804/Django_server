# 목차(Contents List)를 Dictionary로 바꿀 때 사용
# 기본적으로 소문자로 변환해서 사전에 추가하고 그럼
from kiwipiepy import Kiwi
from make_dic import make_dictionary
import time

class IOHandler:
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


# 리스트(목차) 받아서 사전화 (영어는 소문자로 transform_List_English2Lower 함수)
def add_Dictionary(path, contents_list, flag):
    # flag = a: 이어쓰기 / w: 새로만들어쓰기 / r: 읽기
    c_list = transform_List_English2Lower(contents_list)

    with open(path, flag, encoding='utf8') as f:
        # kiwi.add_user_word(word, 'NNP', 3.0)
        for word in c_list:
            data = '\n' + word + '\t' + 'NNP' + '\t' + '3.0'
            f.write(data)


# 원본
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



kiwi = Kiwi()

c_list_path = "./server_project/search_app/doc_data/iGate_Contents_list.docx"
c_list = make_dictionary(c_list_path, 0)


dic_path = "./server_project/search_app/doc_data/new_dict.txt"
sentence = 'iManager Architecture 지정변경법 가르쳐주세요.'


#add_Dictionary(dic_path, c_list, 'a')
kiwi.load_user_dictionary(dic_path)
kiwi.prepare()
result = kiwi.analyze(transform_Sentence_English2Lower(sentence), 1)
print(result)


"""
handle = IOHandler('test.txt', 'result.txt')
kiwi.analyze(handle.read, handle.write)
"""

