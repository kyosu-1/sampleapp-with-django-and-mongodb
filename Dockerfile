FROM python:3.9-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

RUN apt-get update

# install dependencies
RUN python3 -m pip install --upgrade pip setuptools

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000
