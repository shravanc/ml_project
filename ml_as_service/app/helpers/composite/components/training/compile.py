from app.helpers.composite.components.component import Component

class Compile(Component):
  def __init__(self):
    self.model = None
    self.data  = None
  
  def operation(self, obj):
    print("---Compile called---")
    self.model = obj.model
    self.data = obj.data

    self.__compile()

    return self


  def __compile(self):
    import tensorflow as tf
    optimizer = tf.keras.optimizers.RMSprop(0.001)

    self.model.compile(
        loss='mse',
        optimizer=optimizer,
        metrics=['mse', 'mae']
    )

    print("****COMPILED****")

