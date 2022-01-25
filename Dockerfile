# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN mkdir -p /code/static
RUN python3 manage.py collectstatic --no-input
COPY . /code/
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:$PORT oc_lettings_site.wsgi:application
