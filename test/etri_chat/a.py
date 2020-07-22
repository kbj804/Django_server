# 잠시멈춤
import os

import tensorflow as tf
import numpy as np
import pandas as pd

from absl import app, flags, logging

FLAGS = flags.FLAGS
flags.DEFINE_string('dataset', '/tmp/pts/data/dataset.csv', 'Dataset path')
flags.DEFINE_string('checkpoint_dir', '/tmp/pts/ckpts', 'Checkpoint directory')
flags.DEFINE_string('model_version', '0000', 'Model version')
flags.DEFINE_string('model_dir', '/tmp/pts/model/0000', 'Model directory')
flags.DEFINE_bool('is_train', True, 'Training mode')
flags.DEFINE_integer('num_epochs', 3, 'Number of epoch')


class DataLoader:
  def __init__(self, data):
    """
    DataLoader class.

    Args:
        data (pandas.DataFrame): Data in Pandas DataFrame format.
    """

    self.data = data

    # User-customized data.
    self.inputs = None
    self.outputs = None
    self.prepare_data()

  def prepare_data(self):
    """
    Prepare data for training a graph.

    Returns:
        Input/output data in numpy array.
    """

    # Convert the first column to datetime type.
    self.data.ix[:, 0] = pd.to_datetime(self.data.ix[:, 0])

    # Sort by the date.
    self.data = self.data.sort_values(0)

    # Get 8 rows as input, and set the row three after as output.
    data_np = self.data.values[::, 1:]
    inputs = []
    outputs = []
    for i in range(len(data_np) - 8 - 3):
      input = data_np[i:i + 8].flatten()
      output = data_np[i + 8 + 3].flatten()

      inputs.append(input)
      outputs.append(output)

    inputs = np.array(inputs)
    outputs = np.array(outputs)
    inputs = inputs.reshape(-1, 8, 170)

    self.inputs = inputs
    self.outputs = outputs

  def get_batch(self, batch_size=64, shuffle=True):
    """
    Get batch samples of the shuffled dataset.

    Args:
        batch_size (int): Batch size.
        shuffle (boolean): If shuffle or not.

    Returns:
        Sample of batch size.
    """

    # Shuffle data.
    if shuffle:
      shuffle_index = np.arange(len(self.inputs))
      np.random.shuffle(shuffle_index)

      shuffled_inputs = self.inputs[shuffle_index]
      shuffled_outputs = self.outputs[shuffle_index]
    else:
      shuffled_inputs = self.inputs
      shuffled_outputs = self.outputs

    # Enumerate.
    n_iter = int(shuffled_inputs.shape[0] / batch_size)
    for i in range(n_iter):
      yield shuffled_inputs[i * batch_size: (i + 1) * batch_size], \
            shuffled_outputs[i * batch_size: (i + 1) * batch_size]


class TensorFlowModel():
  def __init__(self, checkpoint_dir, model_dir, model_version):
    """
    Build graph and export a model.
    """
    self.X = None
    self.Y = None
    self.loss = None
    self.train = None
    self.output = None
    self.model_dir = model_dir
    self.model_version = model_version
    self.checkpoint_dir = checkpoint_dir
    self.checkpoint_path = os.path.join(checkpoint_dir, model_version)

  def build_graph(self):
    """
    Build a graph
    """

    # Define inputs and outputs
    seq_length = 8
    num_links = 170
    hidden_size = 128
    learning_rate = 0.01
    self.X = tf.placeholder(tf.float32, shape=[None, seq_length, num_links],
                            name='X')
    self.Y = tf.placeholder(tf.float32, shape=[None, num_links])

    # build a LSTM network
    cell = tf.contrib.rnn.BasicLSTMCell(
      num_units=hidden_size, state_is_tuple=True, activation=tf.tanh)
    outputs, _states = tf.nn.dynamic_rnn(cell, self.X, dtype=tf.float32)
    # We use the last cell's output
    Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], num_links,
                                               activation_fn=None)

    # cost/loss
    self.loss = tf.reduce_sum(
      tf.square(Y_pred - self.Y))  # sum of the squares

    # optimizer
    optimizer = tf.train.AdamOptimizer(learning_rate)
    self.train = optimizer.minimize(self.loss)

    self.output = Y_pred

  def train_graph(self, loader):
    """
    Train a graph
    """

    saver = tf.train.Saver()

    with tf.Session() as sess:
      init = tf.global_variables_initializer()
      sess.run(init)

      # restore from checkpoint file
      ckpt_state = tf.train.get_checkpoint_state(self.checkpoint_dir)
      if ckpt_state is not None:
        latest_ckpt_path = ckpt_state.model_checkpoint_path
        logging.info('Restore model from {}'.format(latest_ckpt_path))
        saver.restore(sess, latest_ckpt_path)

      num_epochs = FLAGS.num_epochs
      num_batch = 10
      for i in range(num_epochs):
        batch_loader = loader.get_batch(batch_size=num_batch, shuffle=False)
        for inputs, outputs in batch_loader:
          _, loss = sess.run([self.train, self.loss],
                             feed_dict={self.X: inputs, self.Y: outputs})
        logging.info('Train lose: {}'.format(loss))

      # checkpoint save
      saver.save(sess, self.checkpoint_path)
      # tensorflow serving model export
      self.export(sess)
      sess.close()

    tf.reset_default_graph()

  def export(self, session):
    """
    Export a model.
    """

    builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(
      self.model_dir)
    signature = tf.compat.v1.saved_model.predict_signature_def(
      inputs={'in1': self.X},
      outputs={'out1': self.output}
    )
    builder.add_meta_graph_and_variables(
      session,
      tags=[tf.compat.v1.saved_model.tag_constants.SERVING],
      signature_def_map={'predict_speed': signature})
    builder.save()
    logging.info('Save model to {}'.format(self.model_dir))
    logging.info('  in1: {}'.format(self.X.name))
    logging.info('  out1: {}'.format(self.output.name))


def main(argv):
  logging.info('Load dataset')
  df = pd.read_csv(FLAGS.dataset, header=None)

  logging.info('Initialize a DataLoader')
  loader = DataLoader(df)

  if FLAGS.is_train:
    logging.info('Train a model')
    model = TensorFlowModel(FLAGS.checkpoint_dir, FLAGS.model_dir,
                            FLAGS.model_version)
    model.build_graph()
    model.train_graph(loader)
  else:
    pass


if __name__ == '__main__':
  app.run(main)