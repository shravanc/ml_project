from lib.composite.components.component import Component

class Extract(Component):
  def __init__(self):
    self.url = None

  def operation(self, obj):
    self.url = obj
    self.__download()
    print("---Download---")
    return self

  def __download(self):
    import tensorflow as tf
    self.filename = tf.keras.utils.get_file('heart.csv', self.url)
    return
