FROM python:3.11-slim-bullseye as backend

RUN apt-get update && apt-get upgrade -y

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . /app

# This command should be suitable for production use.
# The docker-compose.yml file overrides this command and uses uvicorn directly.
CMD gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000

FROM backend as celery
CMD celery -A backend worker -l INFO
