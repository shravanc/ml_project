from lib.composite.components.component import Component

class Local(Component):
  DEFAULT = "/home/shravan/tf/all_models/temp/serving_model/1/"
  #DEFAULT = "/home/shravan/tf/all_models/temp/"
  def __init__(self, path=DEFAULT):
    self.model  = None
    self.path   = path

  def operation(self, obj):
    self.model = obj.model
    self.data  = obj.data

    self.__save()

    return self

  def __save(self):
    import tensorflow as tf
    #self.model.save( self.path )
    tf.saved_model.save(self.model, self.path )
    return

