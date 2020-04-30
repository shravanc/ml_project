from app.helpers.composite.components.component import Component

class Analyse(Component):
  def __init__(self):
    self.describe           = None
    self.numerical_values   = []
    self.categorical_values = []
    self.keys               = []
    self.target_col         = None


  def operation(self, obj):
    print("---Analyse called---")
    self.df = obj.df
    self.keys = self.df.keys()
    self.target_col = obj.target_col

    self.__analyse()
    return self

  def __analyse(self):
    self.describe = self.df.describe()
    self.numerical_values   = self.describe.keys()   
    self.categorical_values = list(set(self.keys) - set(self.numerical_values))

    

    print(self.describe)
