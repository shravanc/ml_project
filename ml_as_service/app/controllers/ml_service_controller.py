from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from app import upload_path

from app.helpers.params import Params
from app.helpers.template.launch import Launch
from app.models.registry import Registry
from app import db

def index():
  rgs = Registry.query.all()
  registries = []
  print(rgs)

  for rg in rgs:
    registries.append(rg.serialize())


  return jsonify({"data": registries})

def fetch_model():
  return jsonify({})


def train_and_serve():

  params = __get_params()
  launch = Launch()
  launch.launch_template( params )
  __save_to_db( params )

  return jsonify({"received": "call"})


def serve():
  return jsonify({})


# Private methods

def __get_params():

  upload_file = __save_file()
  target_column = request.form['target_column']

  return Params(
    table      = Registry(),
    db         = db,
    url        = upload_file,
    target_col = target_column,
  )

def __save_file():
  upload_file       = request.files['file']
  filename          = secure_filename(upload_file.filename)
  absolute_filepath = os.path.join(upload_path, filename)

  upload_file.save( absolute_filepath )
  return absolute_filepath 


"""
data = {"target_column": target_column}
registry = Registry(categories=data) 
db.session.add(registry)
db.session.commit()
"""
def __save_to_db(params):
  db.session.add(params.table)
  db.session.commit()
