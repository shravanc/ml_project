from app.helpers.composite.components.component import Component

class Extract(Component):
  def __init__(self):
    self.url = None

  def operation(self, obj):
    print("---Extract---")
    self.url = obj
    self.__download()
    return self

  def __download(self):
    import tensorflow as tf
    self.filename = tf.keras.utils.get_file('heart.csv', self.url)
    return
