# Backend/Django
This is a Django project created with `django-admin startproject backend`.

## Dependencies/Virtual Environment
This project uses `pip` and `venv` to manage the virtual environment. To install dependencies locally:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
If you wish to use `pipenv` or `poetry` instead, be sure to update `backend/Dockerfile` to install dependencies using your preferred package manager.

## Settings
Settings use `django-environ` and environment variables to set values which differ  between environments. Copy `.env.dist` into a `.env` file and update the values to match your needs. Notably you should change `SECRET_KEY`, at least for your production environment if not all environments. You may generate a new `SECRET_KEY` using the included `django-extensions` `generate_secret_key` command:
```
source venv/bin/activate
source .env
python manage.py generate_secret_key
```

## User Model
There is an empty custom user model in `backend/models.py`.

## Celery
Celery is configured to read settings from the Django settings module. It will read settings prefixed with `CELERY_`. There is a sample Celery task in `backend/tasks.py`.

## Static Files
[WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) is used for serving static files. If you are unfamiliar, WhiteNoise is particularly useful for hosting Django on PaaS as it allows the app to serve its own static files. It can compress assets with gzip and Brotli as well as deal with the multitude of cache headers. It even plays nice with CDNs. If you don't want to use it, you will need to uninstall it with `pip`, remove the middleware from `settings.py`, and use Django's `runserver` command instead of `gunicorn` and `uvicorn`.