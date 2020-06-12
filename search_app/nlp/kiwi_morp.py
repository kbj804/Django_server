from sklearn.feature_extraction.text import TfidfVectorizer
from kiwipiepy import Kiwi

###### 지금 음 클래스화 해서 불러오는거 해봐야할듯 계속 오류남 오류 고쳐야댐 


# 문장에서 형태소를 뽑아냄
def generate_morp_word(sentence, analyze_num):
    try:
        result = kiwi.analyze(sentence, analyze_num)
        print(result)
        morp_word_list =[]
        morp_nn_list=[]
        morp_vv_list=[]

        for i in range(0, analyze_num):
            morp_word = ''
            morp_nn=''
            morp_vv=''
            #print(i)
            for word in result[i][0]:
                morp_word += word[0]
                morp_word += ' '
                if word[1] in ['NNG','NNP','NNB','NP','SL','SN']:
                    morp_nn += word[0]
                    morp_nn += ' '
                elif word[1] in ['VV','VA','VX','VCP','VCN']:
                    morp_vv += word[0]
                    morp_vv += ' '

            morp_word_list.append(morp_word)
            morp_nn_list.append(morp_nn)
            morp_vv_list.append(morp_vv)
        return morp_word_list, morp_nn_list, morp_vv_list

    except:
        print("### ERROR 형태소 분석기 부분 에 뭐가 잘못된게 있는듯 ERROR ### ")


def get_all_token(sen):
    morp_list, _, _ = generate_morp_word(sen, 1)
    return morp_list


def get_noun(sen):
    print(sen)
    _, nn_list, _ = generate_morp_word(sen, 1)
    return nn_list


def get_vv(sen):
    _, _, vv_list = generate_morp_word(sen, 1)
    return vv_list


if __name__ == "__main__":
    kiwi = Kiwi()
    dic_path = "./server_project/search_app/doc_data/new_dict.txt"
    kiwi.load_user_dictionary(dic_path)

    #kiwi.add_user_word('iXVDR', 'NNP', 3.0)

    kiwi.prepare()

    
    
