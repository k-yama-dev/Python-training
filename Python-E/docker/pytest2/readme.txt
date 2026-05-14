mkdir pytest
cd pytest

#Dockerfile
FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab

#compose.yaml
version: '3'
services:
  python3:
    restart: always
    build: .
    container_name: 'python3'
    working_dir: '/root/'
    tty: true
    volumes:
      - ./opt:/root/opt


mkdir opt
cd opt
#sample.py
import math
import sys

def main():
  val = float(sys.argv[1])
  print(math.radians(val))

if __name__ == "__main__":
  main()

docker compose up -d --build
docker image ls
docker container ls
docker compose exec python3 /bin/bash
python opt/sampke.py 180.0
3.141592653589793
exit
docker compose down
docker container ls