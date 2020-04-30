from app.helpers.composite.components.component import Component

class Extract(Component):
  def __init__(self):
    self.url        = None
    self.target_col = None

  def operation(self, obj):
    self.url        = obj.url
    self.target_col = obj.target_col

    self.__download()
    return self

  def __download(self):
    import tensorflow as tf
    
    self.filename = self.url #tf.keras.utils.get_file('heart.csv', self.url)
    return

