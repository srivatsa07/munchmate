#!/bin/sh
python3 manage.py migrate
exec gunicorn MunchMate.wsgi:application --bind 0.0.0.0:8000
