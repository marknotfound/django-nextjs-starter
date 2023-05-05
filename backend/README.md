This is a Django project created with `django-admin startproject backend`.

# Virtual Environment
This project uses `pip` and `venv` to manage the virtual environment. To install dependencies locally:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
If you wish to use `pipenv` or `poetry` instead, be sure to update `backend/Dockerfile` to install dependencies using your preferred package manager.

# Settings
Settings used `django-environ` and environment variables to set values which differ  between environments. Copy `.env.dist` into a `.env` file and update the values to match your needs. Notably you should change `SECRET_KEY`, at least for your production environment if not all environments. You may generate a new `SECRET_KEY` using the included `django-extensions` command:
```
source venv/bin/activate
source .env
python manage.py generate_secret_key
```
