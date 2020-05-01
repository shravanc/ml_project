from app.helpers.composite.components.component import Component

class Analyse(Component):
  def __init__(self):
    self.params             = None
    self.describe           = None

  def operation(self, obj):
    print("---Analyse called---")
    self.params = obj.params
    self.df = obj.df
    self.params.table.keys = self.df.keys()

    self.__analyse()
    return self

  def __analyse(self):
    self.describe = self.df.describe()
    self.params.table.num_val = self.describe.keys()   
    self.params.table.cat_val = list(set(self.params.table.keys) - \
                                     set(self.params.table.num_val))

    print(self.describe)
