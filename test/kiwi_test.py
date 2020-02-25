# kiwi 형태소 분석기 오픈소스중에서는 가장 빠름 (분류 정확도는 잘 모르겠음 아직 0224 )
from kiwipiepy import Kiwi

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

kiwi = Kiwi()
kiwi.load_user_dictionary(r'./server_project/test/userDict.txt')
kiwi.add_user_word('iXVDR', 'NNP', 3.0)

kiwi.prepare()
# handle = IOHandler(r'./server_project/test/input.txt', r'./server_project/test/result.txt')
# kiwi.analyze(handle.read, handle.write)


result = kiwi.analyze('강남에서 먹었던 오늘의 스파게티는 맛있었다.', 1)
for i in result:
    print(i)


class ReaderExam:
    def __init__(self, filePath):
        self.file = open(filePath, encoding='UTF8')
    
    def read(self, id):
        if id == 0: self.file.seek(0)
        return self.file.readline()

reader = ReaderExam(r'./server_project/test/input.txt')
print(kiwi.extractWords(reader.read, 1, 10, 0.25))
#kiwi.extract_add_words(reader.read, min_cnt = 1, max_word_len = 10, min_score = 0.25, pos_score = -3)


