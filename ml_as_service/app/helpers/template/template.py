from app.helpers.composite.composite import Composite

from abc import ABC, abstractmethod


class Template:
  def __init__(self):
    self.tree     = Composite()
    self.branches = []
    self.url      = None

  def launch_template(self, url):
    self.url = url

    self.branches.append(self.etl())
    self.branches.append(self.eda())
    self.branches.append(self.model())
    self.branches.append(self.train())
    self.branches.append(self.save())
    self.branches.append(self.serve())

    self.add_branches()
    self.operate()

    return self.response_format()


  def add_branches(self):
    for branch in self.branches:
      self.tree.add(branch)

  def operate(self):
    self.resp = self.tree.operation( self )

  def response_format(self):
    return self.resp

  @abstractmethod
  def text_data(self):
    pass

  @abstractmethod
  def prediction(self):
    pass

  @abstractmethod
  def train(self):
    pass



