#!/bin/sh
set -e
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

python main.py
#gunicorn -c gunicorn.config.py wsgi:app


