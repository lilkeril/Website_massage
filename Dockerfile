FROM python:3.10-slim-buster
RUN python -m pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install postgresql-client -y
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /.
