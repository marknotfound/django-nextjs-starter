#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
uvicorn backend.asgi:application --reload --host 0.0.0.0
