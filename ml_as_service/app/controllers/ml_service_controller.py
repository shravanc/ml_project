from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from app import upload_path

from app.helpers.template.launch import Launch

def index():
  return jsonify({})

def fetch_model():
  return jsonify({})

def train_and_serve():
  upload_file = request.files['file']
  target_column = request.form['target_column']
  filename = secure_filename(upload_file.filename)
  absolute_filepath = os.path.join(upload_path, filename)
  upload_file.save( absolute_filepath )


  launch = Launch()
  launch.launch_template( absolute_filepath, target_column)

  return jsonify({"received": "call"})

def serve():
  return jsonify({})

