import tensorflow as tf

tf.app.flags.DEFINE_string('train_dir', './train', 'train directory')
tf.app.flags.DEFINE_string('model_dir', './model/0000', 'model directory')
tf.app.flags.DEFINE_string('log_dir', './logs', 'log directory')
tf.app.flags.DEFINE_string('ckpt_name', 'chat.ckpt', 'checkpoint name')

tf.app.flags.DEFINE_boolean('train', False, 'start train')
tf.app.flags.DEFINE_boolean('test', True, 'start test')
tf.app.flags.DEFINE_boolean('data_loop', True, 'test the mini dataset')
tf.app.flags.DEFINE_integer('batch_size', 100, 'mini batch size')
tf.app.flags.DEFINE_integer('epoch', 300, 'number of epoch')

tf.app.flags.DEFINE_string('data_path', './data/chat.log', 'the data path')
tf.app.flags.DEFINE_string('voc_path', './data/chat.voc', 'vocabulary')
tf.app.flags.DEFINE_boolean('voc_test', False, 'test the vocabulary')
tf.app.flags.DEFINE_boolean('voc_build', False, 'build the voca using the dialog')

tf.app.flags.DEFINE_integer('max_decode_len', 30, 'maximumn size of answers')

FLAGS = tf.app.flags.FLAGS