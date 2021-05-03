FROM centos:7

EXPOSE 5000

RUN yum install -y python3

RUN /bin/pip3 install --upgrade pip

COPY . /usr/src/app

RUN /bin/pip3 install -r /usr/src/app/requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:5000/memory || exit 1

ENTRYPOINT /usr/src/app/stats_collector.py
