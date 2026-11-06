FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY . /app

CMD ["python3", "app.py"]
