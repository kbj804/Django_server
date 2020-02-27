from gensim.models.word2vec import Word2Vec
import ast
import pandas as pd

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def create_model(filename, skip_gram=False):
    tokens = pd.read_csv(filename)
    tokens = tokens[tokens["contents"].apply(lambda x: 'http' not in x)]

    sentence = tokens["token"].apply(lambda x: ast.literal_eval(x)).tolist()

    if skip_gram:
        model = Word2Vec(sentence, min_count=3, iter=20, size=300, sg=1)
    else:
        model = Word2Vec(sentence, min_count=3, iter=20, size=300, sg=0)

    model.init_sims(replace=True)
    model.save(r"./server_project/test/kakao_reg/embedding_nn.model")


def most_similar(word):
    model = Word2Vec.load(r"./server_project/test/kakao_reg/embedding_nn.model")

    return model.most_similar(word)


if __name__ == '__main__':
    #create_model(r"./server_project/test/kakao_reg/noun_token.csv")

    word = '죽'
    r = most_similar(word)
    print(r)