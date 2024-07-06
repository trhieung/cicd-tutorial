FROM python:3.10-alpine

RUN apk update && apk add python3-dev gcc libc-dev curl

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn

ADD ./compose /app/compose
ADD ./env /app/env
ADD ./services /app/services

RUN pip install -r /app/services/requirements/base.txt

RUN chmod +x /app/compose/server/server-entrypoint.sh