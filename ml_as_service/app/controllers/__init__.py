import os
from flask import Blueprint, current_app

# Imports
from app.controllers.landing_controller import home as landing_home

from app.controllers.users_controller import signup as users_signup
from app.controllers.users_controller import signup as users_signin

from app.controllers.dashboard_controller import index as dashboard_index

from app.controllers.ml_service_controller import index            as ml_service_index
from app.controllers.ml_service_controller import fetch_model      as ml_service_fetch_model
from app.controllers.ml_service_controller import train_and_serve  as ml_service_train_and_serve
from app.controllers.ml_service_controller import serve            as ml_service_serve



# Blueprints
landing_template      = os.path.abspath('app/views/landing')
landing_blueprints    = Blueprint('home', 'api', template_folder=landing_template)
                     
user_template         = os.path.abspath('app/views/users')
users_blueprints      = Blueprint('users', 'api', template_folder=user_template)

dashboard_template    = os.path.abspath('app/views/dashboard')
dashboard_blueprints  = Blueprint('dashboard','api', template_folder=dashboard_template)

ml_service_template   = os.path.abspath('app/views/ml_service')
ml_service_blueprints = Blueprint('ml_service','api', template_folder=ml_service_template)



# Routes
landing_blueprints.add_url_rule('/', view_func=landing_home, methods=['GET'])

users_blueprints.add_url_rule('/signup', view_func=users_signup, methods=['GET'])
users_blueprints.add_url_rule('/signin', view_func=users_signin, methods=['GET'])

dashboard_blueprints.add_url_rule('/dashboard', view_func=dashboard_index, methods=['GET'])

ml_service_blueprints.add_url_rule('/services',         view_func=ml_service_index, methods=['GET'] )
ml_service_blueprints.add_url_rule('/fetch_model',      view_func=ml_service_fetch_model, methods=['GET'] )
ml_service_blueprints.add_url_rule('/train_and_serve',  view_func=ml_service_train_and_serve, methods=['POST'] )
ml_service_blueprints.add_url_rule('/registry/<_id>/serve',            view_func=ml_service_serve, methods=['POST'] )

