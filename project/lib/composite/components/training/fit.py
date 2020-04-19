from lib.composite.components.component import Component

class Fit(Component):
  def __init__(self):
    self.model = None
    self.data  = None

  def operation(self, obj):
    print("---Fit called---")
    self.model = obj.model
    self.data  = obj.data

    self.__fit()
    return self


  def __fit(self):
    self.model.fit(
        self.data.x, 
        self.data.y, 
        epochs=10,
        callbacks=self.data.visualize,
    )
