from app.helpers.composite.components.component import Component

class Analyse(Component):
  def __init__(self):
    self.describe = None

  def operation(self, obj):
    print("---Analyse called---")
    self.df = obj.df

    self.__analyse()
    return self

  def __analyse(self):
    self.describe = self.df.describe()
    print(self.describe)
