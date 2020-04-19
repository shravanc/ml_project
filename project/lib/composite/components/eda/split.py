from lib.composite.components.component import Component

class Split(Component):
  def __init__(self):
    self.df = None
    self.x = None
    self.y = None
    self.eval_x = None
    self.eval_y = None
    self.visualize = []

  def operation(self, obj):
    print("---Split---")
    self.df = obj.df

    self.__split()
    return self


  def __split(self):
    self.x      = self.df.sample(frac=0.8, random_state=0)
    self.eval_x = self.df.drop( self.x.index )

    self.y      = self.x.pop('target')
    self.eval_y = self.eval_x.pop('target')


    self.train_stats = self.x.describe()
    self.train_stats = self.train_stats.transpose()
    print(self.train_stats)
