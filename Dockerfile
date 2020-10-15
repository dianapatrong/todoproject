FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
RUN apk add postgresql-dev gcc musl-dev
COPY . /code/
RUN pip install -r requirements.txt
