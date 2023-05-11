# syntax=docker/dockerfile:1

FROM arm32v7/python:3.7.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]
