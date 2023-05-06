# Django Next.js Starter
This project provides a quickstart to develop a project with a Next.js frontend served by a Django backend. Out of the box, it includes:
* **Next.js 13.4** + TypeScript app created with `npx create-next-app`
* **Django 4.2** project created with `django-admin startproject`
  * Preconfigured with
    * Postgres
    * Redis
    * Celery

The Django and Next.js projects are located in the `backend` and `client` directories respectively. See `backend/README.md` and `client/README.md` for more information about how to configure them.

Django will run at `http://localhost:8000` and Next.js will run at `http://localhost:3000`.

## Environment Variables
Both Django and Next.js make use of environment variables. There is a `.env.dist` file in both the `backend` and `client` directories. You must copy this file into the relevant environment files:
```
cp backend/.env.dist backend/.env
cp client/.env.dist client/.env.local
```

## Docker
`docker-compose.yml` defines all of the backend services. You may comment out or remove services which aren't needed. It is preconfigured with Postgres, Redis, and Celery which is a fairly standard Django stack.

The `backend/Dockerfile` is used for the `backend` and `celery` services. It is, in my opinion, suitable for production use, but open a pull request if something looks off.

## Deploying
This repo is generally unopinionated on deploying. I unofficially recommend [Vercel](https://vercel.com/) for Next.js and [Railway](http://railway.app/) for Django. Both support monorepos such as this by allowing you to specify a root directory. Ultimately it is up to you how you want to deploy. The backend uses `DATABASE_URL` and `REDIS_URL` environment variables which are commonly used in PaaS offerings.