from app.helpers.composite.components.component import Component

class ClusterImputation(Component):
  def __init__(self):
    pass

  def operation(self, obj):
    print("---ClusterImputation---")
    self.__cluster_impute()
    return self

  def __cluster_impute(self):
    pass
