
from tensorflow as tf
from app.helpers.composite.components.component import Component

class Adam:(Component):
  EPOCHS = 10
  def __init__(self, epochs=EPOCHS):
    self.model  = None
    self.x      = None
    self.y      = None
    self.epochs = epochs

  def operation(self, obj):

    self.model  = obj.model
    self.x      = obj.x
    self.y      = obj.y

    self.model.compile(loss='binary_crossentropy',
                       optimizer="adam",
                       metrics=["accuracy"])

    self.model.fit(self.x, self.y, epochs=self.epochs)
    return self


