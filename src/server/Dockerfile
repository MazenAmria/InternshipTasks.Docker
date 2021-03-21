FROM python:3.7-alpine

EXPOSE 5000

RUN pip install --upgrade pip

COPY . /usr/src/app

RUN apk add --update --no-cache gcc linux-headers musl-dev

RUN pip install -r /usr/src/app/requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:5000/memory || exit 1

ENTRYPOINT /usr/src/app/start.sh
