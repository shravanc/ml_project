
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Registry(db.Model):
  __tablename__ = 'registries'

  id = db.Column(db.Integer, primary_key=True)
  target_col  = db.Column(db.String)
  url         = db.Column(db.String)
  keys        = db.Column(db.ARRAY(db.String(120)))
  num_val     = db.Column(db.ARRAY(db.String(120)))
  cat_val     = db.Column(db.ARRAY(db.String(120)))
  categories  = db.Column(JSON)


  def __init__(self, categories=[], target_col="", url="", keys=[], num_val=[], cat_val=[] ):
    
    self.target_col = target_col
    self.keys       = keys
    self.num_val    = num_val
    self.cat_val    = cat_val

    self.categories = categories
    


  def __repr__(self):
    return '<id {}>'.format(self.id)
    

  def serialize(self):
      return {
          'id': self.id,
          'target_col': self.target_col,
          'url': self.url,
          'keys': self.keys,
          'num_val': self.num_val,
          'cat_val': self.cat_val, 
          'categories': self.categories,
      }
