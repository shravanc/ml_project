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
  filename = secure_filename(upload_file.filename)
  upload_file.save(os.path.join(upload_path, filename))

  return jsonify({"received": "call"})

def serve():
  return jsonify({})

