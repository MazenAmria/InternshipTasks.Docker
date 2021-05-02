FROM centos:7

EXPOSE 5000

RUN yum install -y cronie python3

RUN ln /usr/bin/python3 /usr/bin/python -f
RUN ln /usr/bin/pip3 /usr/bin/pip -f

RUN pip install --upgrade pip

COPY . /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:5000/memory || exit 1

ENTRYPOINT /usr/src/app/start.sh
