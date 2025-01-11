FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc g++ build-essential

COPY ./requirements.txt /opt/requirements.txt
RUN pip --no-cache-dir install -r /opt/requirements.txt