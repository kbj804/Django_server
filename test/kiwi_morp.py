# https://github.com/bab2min/kiwipiepy
# 그냥 정리해놓은거 - 실행파일 아님

from kiwipiepy import Kiwi, Option
kiwi = Kiwi()


"""
num_thread가 2 이상이면 단어 추출 및 형태소 분석에 멀티 코어를 활용하여 조금 더 빠른 속도로 분석을 진행할 수 있습니다. 
num_thread가 1인 경우 단일 코어만 활용합니다. num_thread가 0이면 현재 환경에서 사용가능한 모든 코어를 활용합니다. 
생략 시 기본값은 0입니다.
"""
Kiwi(num_thread=0, model_path='./', options=Option.LOAD_DEFAULT_DICTIONARY | Option.INTEGRATE_ALLOMORPH)

"""
options은 Kiwi 실행시에 설정한 다양한 옵션들을 세팅하는 비트 마스크 값입니다. 사용 가능한 값은 다음과 같습니다.

Option.LOAD_DEFAULT_DICTIONARY : 추가 사전을 로드합니다. 추가 사전은 위키백과의 표제어 타이틀로 구성되어 있습니다. 
                                이 경우 로딩 및 분석 시간이 약간 증가하지만 다양한 고유명사를 좀 더 잘 잡아낼 수 있습니다.
Option.INTEGRATE_ALLOMORPH : 어미 중, '아/어', '았/었'과 같이 동일하지만 음운 환경에 따라 형태가 달라지는 이형태들을 
                            자동으로 통합합니다.
"""

### kiwi 객체는 크게 다음 세 종류의 작업을 수행할 수 있습니다.

# 1 코퍼스로부터 미등록 단어 추출
# 2 사용자 사전 추가
# 3 형태소 분석

# 미등록 단어추출 관련 메소드 3가지
# 1-1.
# kiwi.extract_words(reader, min_cnt, max_word_len, min_score)

"""
reader가 읽어들인 텍스트로부터 단어 후보를 추출합니다. reader는 다음과 같은 호출가능한(Callable) 객체여야합니다.
 min_cnt는 추출할 단어가 입력 텍스트 내에서 최소 몇 번 이상 등장하는 지를 결정합니다.
입력 텍스트가 클 수록 그 값을 높여주시는게 좋습니다. 
max_word_len는 추출할 단어의 최대 길이입니다. 이 값을 너무 크게 설정할 경우 단어를 스캔하는 시간이 길어지므로 적절하게 조절해주시는 게 좋습니다. 
min_score는 추출할 단어의 최소 단어 점수입니다. 이 값을 낮출수록 단어가 아닌 형태가 추출될 가능성이 높아지고, 
반대로 이 값을 높일 수록 추출되는 단어의 개수가 줄어들므로 적절한 수치로 설정하실 필요가 있습니다. 기본값은 0.25입니다.
"""

class ReaderExam:
    def __init__(self, filePath):
        self.file = open(filePath)
    
    def read(self, id):
        if id == 0: self.file.seek(0)
        return self.file.readline()

reader = ReaderExam('test.txt')
kiwi.extractWords(reader.read, 10, 10, 0.25)

# 1-2.
# kiwi.extractFilterWords(reader, min_cnt, max_word_len, min_score, pos_score)
# extract_filter_words(reader, min_cnt = 10, max_word_len = 10, min_score = 0.25, pos_score = -3)

"""
extractWords와 동일하게 단어 후보를 추출하고, 그 중에서 이미 형태소 분석 사전에 등록된 경우 및 명사가 아닐 것으로 
예측되는 단어 후보를 제거하여 실제 명사로 예측되는 단어 목록만 추출해줍니다. 
pos_score는 추출할 단어의 최소 명사 점수입니다. 
이 값을 낮출수록 명사가 아닌 단어들이 추출될 가능성이 높으며, 반대로 높일수록 추출되는 명사의 개수가 줄어듭니다. 
기본값은 -3입니다. 나머지 인자는 extractWords와 동일합니다.
"""

# 1-3.
# kiwi.extractAddWords(reader, min_cnt, max_word_len, min_score, pos_score)
# extract_add_words(reader, min_cnt = 10, max_word_len = 10, min_score = 0.25, pos_score = -3)

"""
extractFilterWords와 동일하게 명사인 단어만 추출해줍니다. 
다만 이 메소드는 추출된 명사 후보를 자동으로 사용자 사전에 등록하여 형태소 분석에 사용할 수 있게 해줍니다. 
만약 이 메소드를 사용하지 않으신다면 add_user_word 메소드를 사용하여 추출된 미등록 단어를 직접 사용자 사전에 등록하셔야 합니다.
"""

#  ----------------------------------------------------------------------  #
#  사용자 사전 추가
#  kiwi.add_user_word(word, pos, score)
#  kiwi.load_user_dictionary(userDictPath)

add_user_word(word, pos = 'NNP', score = 0.0)

"""
사용자 사전에 word를 등록합니다. 현재는 띄어쓰기(공백문자)가 포함되지 않는 문자열만 단어로 등록할 수 있습니다. 
pos는 등록할 단어의 품사입니다. 세종 품사태그를 따르며, 기본값은 NNP(고유명사)입니다. score는 등록할 단어의 점수입니다. 
동일한 형태라도 여러 경우로 분석될 가능성이 있는 경우에, 이 값이 클수록 해당 단어가 더 우선권을 가지게 됩니다.
"""

load_user_dictionary(userDictPath)


#  ----------------------------------------------------------------------  #
#  형태소 분석
#  kiwi을 생성하고, 사용자 사전에 단어를 추가하는 작업이 완료되었으면 prepare를 호출하여 분석 모델을 준비

## kiwi.prepare()

#  이 메소드는 별다른 파라미터를 필요로하지 않으며, 성공하였을 경우 0, 실패하였을 경우 0이 아닌 값을 돌려줍니다.
#  실제 형태소를 분석하는 메소드에는 다음이 있습니다.

## kiwi.analyze(text, top_n)
## kiwi.analyze(reader, receiver, top_n)

analyze(text, top_n = 1)
# 입력된 text를 형태소 분석하여 그 결과를 반환합니다. 총 top_n개의 결과를 출력

