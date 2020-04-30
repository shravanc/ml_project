from app.helpers.composite.components.component import Component

class Transform(Component):
  def __init__(self):
    self.filename = None
    self.df       = None
    self.files    = []
    self.target_col = None

  def operation(self, obj):
    self.filename = obj.filename
    self.target_col = obj.target_col

    self.__transform()
    print("---Transorm called---")
    return self


  def __transform(self):
    self.files = [self.filename]
