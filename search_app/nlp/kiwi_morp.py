from sklearn.feature_extraction.text import TfidfVectorizer
from kiwipiepy import Kiwi

class kiwi_dictionary_n_fuction:
    def __init__(self, path):
        self.kiwi = Kiwi()
        self.kiwi.load_user_dictionary(path)
        self.kiwi.prepare()
    
    def get_noun(self,sen):
        print(sen)
        _, self.nn_list, _= self.generate_morp_word(sen, 1)
        return self.nn_list

    def get_all_token(self, sen):
        self.morp_list, _, _ = self.generate_morp_word(sen, 1)
        return self.morp_list

    def get_vv(self,sen):
        _, _, self.vv_list = self.generate_morp_word(sen, 1)
        return self.vv_list

    def get_analyze_result(self, sentence, analyze_num):
        return 

    # 문장에서 형태소를 뽑아냄
    def generate_morp_word(self, sentence, analyze_num):
        try:
            self.result = self.kiwi.analyze(sentence, analyze_num)
            self.morp_word_list =[]
            self.morp_nn_list=[]
            self.morp_vv_list=[]

            for i in range(0, analyze_num):
                morp_word = ''
                morp_nn=''
                morp_vv=''
                #print(i)
                for word in self.result[i][0]:
                    morp_word += word[0]
                    morp_word += ' '
                    if word[1] in ['NNG','NNP','NNB','NP','SL','SN']:
                        morp_nn += word[0]
                        morp_nn += ' '
                    elif word[1] in ['VV','VA','VX','VCP','VCN']:
                        morp_vv += word[0]
                        morp_vv += ' '

                self.morp_word_list.append(morp_word)
                self.morp_nn_list.append(morp_nn)
                self.morp_vv_list.append(morp_vv)
            return self.morp_word_list, self.morp_nn_list, self.morp_vv_list

        except Exception as e:
            print(e)
            print("### ERROR 형태소 분석기 부분 에 뭐가 잘못된게 있는듯 ERROR ### ")