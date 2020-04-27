from lib.template.template import Template

from lib.composite.composite import Composite
from lib.composite.components.etl.data import Data

from lib.composite.components.models.simple     import Simple
from lib.composite.components.training.adam     import AdamTraining
from lib.composite.components.saving.local      import Local


class Train(Template):

  def __init__(self):
    super(Train, self).__init__()

  def text_data(self):
    english_branch = Composite()
    english_branch.add(English())
    english_branch.add(KerasTokenizer())

    return english_branch

  def train(self):
    model_branch = Composite()
    model_branch.add(Simple())
    model_branch.add(AdamTraining())
    model_branch.add(Local())

    return model_branch

