from sklearn.feature_extraction.text import TfidfVectorizer
from kiwipiepy import Kiwi

mydoclist = ['강남 에서 먹 었 던 오늘 의 스파게티 는 맛있 었 다 .','오늘 강남 에서 맛있 는 스파게티 를 먹 었 다 .']
mydoclist2 = ['강남에서 먹었던 오늘의 스파게티는 맛있었다.', '오늘 강남에서 맛있는 스파게티를 먹었다.']

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(mydoclist2)

document_distances = (tfidf_matrix * tfidf_matrix.T)

print('유사도 분석을 위한 ' + str(document_distances.get_shape()[0]) + 'x' + str(document_distances.get_shape()[1]) + ' matrix.')
print(document_distances.toarray())

kiwi = Kiwi()
kiwi.load_user_dictionary(r'./server_project/test/userDict.txt')
#kiwi.add_user_word('iXVDR', 'NNP', 3.0)
#kiwi.add_user_word('ERR2034', 'NNP', 1.0)
kiwi.prepare()

# 문장에서 형태소를 뽑아냄
def generate_morp_word(sentence,analyze_num):
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

sentence = 'Mapping-Rule Designer 어떻게 알아볼 수 있을까?'

morp_list, nn_list, vv_list = generate_morp_word(sentence, 1)

print("형태소 : ", morp_list)
print("명사 : ", nn_list)
print("동사 : ", vv_list)

    
    
