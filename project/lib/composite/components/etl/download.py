from lib.composite.components.component import Component

import tensorflow as tf

# https://storage.googleapis.com/applied-dl/heart.csv
class Download(Component):
  def __init__(self):
    self.url = None

  def operation(self, obj):
    self.url = obj
    self.__download()
    print("---Download---")
    return self

  def __download(self):
    self.filename = tf.keras.utils.get_file('heart.csv', self.url)
    return
