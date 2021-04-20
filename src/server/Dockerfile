FROM python:3.9.4-alpine

EXPOSE 5000

RUN pip install --upgrade pip

COPY . /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt

RUN apk add openssh

HEALTHCHECK CMD curl --fail http://localhost:5000/memory || exit 1

ENTRYPOINT /usr/src/app/start.sh
