from app.helpers.composite.components.component import Component

class Preprocess(Component):
  def __init__(self):
    self.params             = None
    self.df                 = None

  def operation(self, obj):
    print("---Preprocess called---")
    self.params = obj.params
    self.df = obj.df

    self.__preprocess()
    return self

  def __preprocess(self):
    #import pandas as pd
    self.__get_categories()
    self.__replace()

    """
    for cat in self.params.table.cat_val:
      self.df[cat] = pd.Categorical(self.df[cat])
      self.df[cat] = self.df[cat].cat.codes
    print(self.df.head())
    """

  def __get_categories(self):
    categories = []
    for cat in self.params.table.cat_val:
      data = {}
      data['col'] = cat

      unique_val = self.df[cat].unique()
      print("unique_val--->", unique_val)
      cat = {}
      for i, val in enumerate(unique_val):
        cat[val] = i
      data['categories'] = cat
      categories.append(data)

    self.params.table.categories = categories

  def __replace(self):
    print(self.params.table.categories)
    for cat in self.params.table.categories:
      print(cat)
      print(cat['col'])
      print(cat['categories'])
      self.df[cat['col']] = self.df[cat['col']].replace(cat['categories'])
