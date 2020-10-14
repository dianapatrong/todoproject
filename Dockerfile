FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk add postgresql-dev gcc musl-dev
RUN pip install -r requirements.txt
COPY . /code/
