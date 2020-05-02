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


def serve(_id):
  data = __format_serve_data(_id)
  __serve_me_please(data)
  return jsonify({"id": _id, "data": data})


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

def __save_to_db(params):
  db.session.add(params.table)
  db.session.commit()


def __format_serve_data(_id):
  from sklearn.preprocessing import StandardScaler, MinMaxScaler
  from sklearn import preprocessing

  #import numpy as np
  params = request.json
  registry = Registry.query.get(_id)
  params = __categories_features(registry, params)


  data = []
  inp = params["params"]
  for k, v in inp.items():
    data.append(v)

  #print(data)
  scaled_features = preprocessing.normalize([data]) #MinMaxScaler().fit_transform( [data] )
  #print(scaled_features)
  scaled_features = scaled_features.tolist() 
  return scaled_features


def __categories_features(registry, params):
  categorical = registry.cat_val
  categories  = registry.categories
  for cat in categorical:
    for c in categories:
      #print("-----C**********>", c, cat)
      if c['col'] == cat:
        params['params'][cat] = c['categories'][params['params'][cat]]

  return params

def __serve_me_please(data):
  print("tensor---input******>", data)
  r = requests.post("http://localhost:8501/v1/models/saved_model:predict", data = {'instances': data})
  print(r)

