from lib.composite.components.component import Component

class Load(Component):
  def __init__(self):
    self.files = None
  
  def operation(self, obj):
    self.files = obj.files
    self.__load()
    print("---Load called---")
    return self

  def __load(self):
    import pandas as pd
    dfs = []
    for filename in self.files:
      dfs.append(
        pd.read_csv(filename, index_col=None, header=0)
      )

    self.df = pd.concat(dfs, axis=0, ignore_index=True)
    print(self.df.head())
    return
