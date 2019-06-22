FROM python:3.7-alpine

# Updates and installations:
RUN pip install pipenv

# Setup working directory:
WORKDIR /app

## Install requirements:
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy

COPY . /app

CMD ["pipenv", "run", "gunicorn", "wsgi:app"]