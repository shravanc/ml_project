from app.helpers.composite.components.component import Component

import tensorflow as tf
#from app import ml_model_path as model_path


class TwoLayeredDenseClassifier(Component):
  DEFAULT = "" #model_path
  NEW_MODEL = True


  def __init__(self, path=DEFAULT, new_model=NEW_MODEL):
    self.data = None
    self.model = None

  def operation(self, obj):
    self.data = obj
    
    self.__model()
    return self

  def __model(self):
    self.model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=[len(self.data.x.keys())] ),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    print(self.model.summary())
    return 
