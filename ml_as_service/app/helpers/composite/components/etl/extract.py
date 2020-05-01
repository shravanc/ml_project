from app.helpers.composite.components.component import Component

class Extract(Component):
  def __init__(self):
    self.params     = None

  def operation(self, obj):
    self.params = obj.params

    self.__download()
    return self

  def __download(self):
    import tensorflow as tf
    
    self.filename = self.params.table.url #tf.keras.utils.get_file('heart.csv', self.url)
    return

