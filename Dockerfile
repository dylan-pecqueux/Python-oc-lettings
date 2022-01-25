# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY .env /.env
COPY . /code/
RUN mkdir -p /code/static
RUN export $(SECRET_KEY .env) && python manage.py collectstatic --no-input
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:$PORT oc_lettings_site.wsgi:application
