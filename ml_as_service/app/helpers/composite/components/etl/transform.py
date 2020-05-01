from app.helpers.composite.components.component import Component

class Transform(Component):
  def __init__(self):
    self.params = None
    self.filename = None
    self.files    = []

  def operation(self, obj):
    print("---Transorm called---")
    self.params     = obj.params
    self.filename   = obj.filename

    self.__transform()

    return self


  def __transform(self):
    self.files = [self.filename]
