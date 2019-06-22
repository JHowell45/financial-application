FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip install pipenv
RUN pipenv install --deploy

ENTRYPOINT ["pipenv", "run", "python"]
CMD ["wsgi.py"]