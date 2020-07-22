from .model import Seq2Seq
from .config import FLAGS
from .dialog import Dialog

import tensorflow as tf
import numpy as np
import json
import math
import os

curr = os.path.dirname(os.path.realpath(__file__))

dialog = Dialog()
dialog.load_vocab(curr + '/data/love.voc')

model = Seq2Seq(dialog.vocab_size)

sess = tf.Session() 
model_path = curr + '/model'
metafile = [f for f in os.listdir(model_path) if 'meta' in f]
saver = tf.train.import_meta_graph(model_path + '/' + metafile[0])
saver.restore(sess, tf.train.latest_checkpoint(model_path + '/'))

def _decode(enc_input, dec_input):
    if type(dec_input) is np.ndarray:
        dec_input = dec_input.tolist()

    input_len = int(math.ceil((len(enc_input) + 1) * 1.5))

    enc_input, dec_input, _ = dialog.transform(enc_input, dec_input,
                                               input_len, FLAGS.max_decode_len)

    return model.predict(sess, [enc_input], [dec_input])

def main_func(x, user_args=None):
    x = json.loads(x)
    enc_input = x['enc_input']
    dec_input = []

    curr_seq = 0
    for i in range(FLAGS.max_decode_len):
        outputs = _decode(enc_input, dec_input)
        if dialog.is_eos(outputs[0][curr_seq]):
            break
        elif dialog.is_defined(outputs[0][curr_seq]) is not True:
            dec_input.append(outputs[0][curr_seq])
            curr_seq += 1

    dec_input = [str(i) for i in dec_input]
    data = {'dec_input': dec_input}

    return json.dumps(data)

#if __name__ == '__main__':
#    x = """{"enc_input": [67]}"""
#    main_func(x)