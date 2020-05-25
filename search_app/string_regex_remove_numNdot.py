# 문자열 정규화 (regex)
# Tree 컬럼의 숫자와 . 을 제거
import pandas as pd 
import re

def remove_num(text):
    return "".join(p.findall(str(text)))

def remove_dot(text, cnt):
    # replace의 경우 . 을 모두 삭제함. Title중 install.sh 같은게 있어도 .을 없애기 때문에 사용X
    # return text.replace(".","")
    return re.sub(pattern='.', repl='', count=cnt, string=text)

def extract_word():
    tree_list = ['Tree1', 'Tree2', 'Tree3']
    for tree in tree_list:

        # 숫자 제거
        df[tree] = df[tree].apply(lambda x: remove_num(x))

        # .(dot) 제거
        if tree == 'Tree2':
            df[tree] = df[tree].apply(lambda x: remove_dot(x, 1))
        elif tree == 'Tree3':
            df[tree] = df[tree].apply(lambda x: remove_dot(x, 2))
        else:
            df[tree] = df[tree].apply(lambda x: remove_dot(x, 0))

        print(df[tree].head(5))


if __name__ == "__main__":
    df = pd.read_excel(r"./server_project/search_app/doc_data/Manual_QnA_Data.xlsx")
    p = re.compile("[^0-9]")
    extract_word()
