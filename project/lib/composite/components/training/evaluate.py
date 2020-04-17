from lib.composite.components.component import Component

class Evaluate(Component):
  def __init__(self):
    self.model = None
    self.data  = None

  def operation(self, obj):
    print("---Evaluate called---")
    self.model = obj.model
    self.data  = obj.data

    self.__evaluate()
    return self

  def __evaluate(self):
    loss, mse, mae = self.model.evaluate( self.data.eval_x, self.data.eval_y, verbose=2 )
    print(f"****Loss: {loss}, MSE: {mse}, MAE: {mae}****")
