class Params:

  def __init__(self, table=None, db=None, url="", target_col=""):
    self.table = table
    self.db    = db

    self.table.url        = url
    self.table.target_col = target_col

