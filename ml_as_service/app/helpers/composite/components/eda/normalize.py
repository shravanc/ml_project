from app.helpers.composite.components.component import Component

class Normalize(Component):
  def __init__(self):
    self.params = None
    self.x = None
    self.y = None
    self.eval_x = None
    self.eval_y = None
  
  def operation(self, obj):
    self.params = obj.params
    self.x = obj.x
    self.y = obj.y
    
    self.eval_x = obj.eval_x
    self.eval_y = obj.eval_y

    self.__scale()
    print("---Scale called---")
    return self

  def __scale(self):
    from sklearn.preprocessing import StandardScaler
    import pandas as pd


    scaled_features = StandardScaler().fit_transform(self.x.values)
    self.x = pd.DataFrame(scaled_features, index=self.x.index, columns=self.x.columns)

    scaled_features = StandardScaler().fit_transform(self.eval_x.values)
    self.eval_x = pd.DataFrame(scaled_features, index=self.eval_x.index, columns=self.eval_x.columns)

    print(self.x.head())
