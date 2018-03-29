FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /bucketlist

WORKDIR /bucketlist

COPY requirements.txt /bucketlist/

RUN pip install -r requirements.txt

COPY . /bucketlist/