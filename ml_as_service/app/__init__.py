from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


path = os.path.abspath(os.path.dirname(__file__)) + "/../instance/development.cfg"
app = Flask(__name__)
app.config.from_pyfile(path)
db = SQLAlchemy(app)
upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'uploads' )
#upload_path = '/home/shravan/tf/upload_path/'

ml_model_path = os.path.abspath(os.path.dirname(__file__)) + '/ml/models/'

def create_app(config_filename=None):
  application = Flask( 'ml_as_service', instance_relative_config=True)
  application.config.from_pyfile(config_filename)
  initialize_extensions(application)
  register_blueprints(application)
  
  return application

def initialize_extensions(application):
  db = SQLAlchemy(application)


def register_blueprints(application):
  from app.controllers import landing_blueprints
  from app.controllers import users_blueprints
  from app.controllers import dashboard_blueprints
  from app.controllers import ml_service_blueprints
  application.register_blueprint( landing_blueprints )
  application.register_blueprint( users_blueprints )
  application.register_blueprint( dashboard_blueprints )
  application.register_blueprint( ml_service_blueprints )




