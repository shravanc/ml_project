from app.helpers.composite.components.component import Component

class Preprocess(Component):
  def __init__(self):
    self.df                 = None
    self.numerical_values   = []
    self.categorical_values = []
    self.keys               = []
    self.target_col         = None



  def operation(self, obj):
    print("---Preprocess called---")
    self.df = obj.df
    self.keys = obj.keys
    self.numerical_values   = obj.numerical_values
    self.categorical_values = obj.categorical_values
    self.target_col         = obj.target_col


    self.__preprocess()
    return self

  def __preprocess(self):
    import pandas as pd

    for cat in self.categorical_values:
      self.df[cat] = pd.Categorical(self.df[cat])
      self.df[cat] = self.df[cat].cat.codes
    print(self.df.head())

