FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    libssl-dev \
    python3-dev \
    cmake \
    gcc

RUN pip install --upgrade pip

CMD [ "python3","app.py" ]