from app.helpers.composite.components.component import Component

import os  


class Visualize(Component):
  DEFAULT = "/tmp/logs"
  TF_LOG  = "/tmp/tf_visualize"

  def __init__(self, default=DEFAULT, tf_logs=TF_LOG):
    self.logdir = default
    self.tf_logs  = tf_logs

  def operation(self, obj):
    print("---Visualize---")
    self.model = obj.model
    self.data  = obj.data

    self.__visualize()
    return self

  def __visualize(self):
    import tensorflow as tf
    self.data.visualize = [tf.keras.callbacks.TensorBoard(
      log_dir=self.logdir,
    )]

    os.system(
      f"nohup tensorboard --logdir={self.logdir} --port=8008 > {self.tf_logs} &"
    )    
    print("***Visualizing***", self.data)
    return
