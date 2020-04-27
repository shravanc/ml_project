from app.helpers.composite.components.component import Component

class Preprocess(Component):
  def __init__(self):
    self.df = None
    self.categprical = ['thal']

  def operation(self, obj):
    print("---Preprocess called---")
    self.df = obj.df
    self.__preprocess()
    return self

  def __preprocess(self):
    import pandas as pd

    for cat in self.categprical:
      self.df[cat] = pd.Categorical(self.df[cat])
      self.df[cat] = self.df[cat].cat.codes
    print(self.df.head())

