from app.helpers.composite.components.component import Component

class Transform(Component):
  def __init__(self):
    self.filename = None
    self.df       = None
    self.files    = []

  def operation(self, obj):
    self.filename = obj.filename

    self.__transform()
    print("---Transorm called---")
    return self


  def __transform(self):
    self.files = [self.filename]
