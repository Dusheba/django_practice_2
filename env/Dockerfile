FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y lsb-release

COPY . /srv/html/djangoPractice
WORKDIR /srv/html/djangoPractice
RUN pip install -r /srv/html/djangoPractice/env/requirements.txt
