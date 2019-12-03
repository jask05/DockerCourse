FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
 
WORKDIR /myapp

COPY app.py /myapp

ENV LOG_PATH=/myapp/logs

