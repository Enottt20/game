#!/bin/sh

python manage.py makemigrations

python manage.py migrate --no-input

python manage.py collectstatic --no-input

cp -r /app/collected_static/. /backend_static/static/

exec gunicorn game.wsgi:application --bind 0.0.0.0:8000