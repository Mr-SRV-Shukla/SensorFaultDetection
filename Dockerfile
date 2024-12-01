FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

COPY requirements.txt .


RUN pip install --upgrade pip

CMD [ "python3","app.py" ]