
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Registry(db.Model):
    __tablename__ = 'registries'

    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(JSON)

    """
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())
    """


    def __init__(self, categories={}):
        self.categories = categories

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'categories': self.categories
        }
