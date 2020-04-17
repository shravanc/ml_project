from lib.composite.components.component import Component

class Impute(Component):
  def __inti__(self):
    self.df = None

  def operation(self, obj):
    print("---Impute called---")
    self.df = obj.df
    self.__impute()

    return self


  def __impute(self):
    print(self.df.isna().sum())
    return
