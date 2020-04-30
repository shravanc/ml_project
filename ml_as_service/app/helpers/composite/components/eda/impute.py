from app.helpers.composite.components.component import Component

class Impute(Component):
  def __inti__(self):
    self.df                 = None
    self.numerical_values   = []
    self.categorical_values = []
    self.keys               = []
    self.target_col         = None


  def operation(self, obj):
    print("---Impute called---")
    self.df   = obj.df
    self.keys = obj.keys
    self.numerical_values   = obj.numerical_values
    self.categorical_values = obj.categorical_values
    self.target_col = obj.target_col



    self.__impute()

    return self


  def __impute(self):
    print(self.df.isna().sum())
    return
