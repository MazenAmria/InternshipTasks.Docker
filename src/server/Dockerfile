FROM centos:7

EXPOSE 5000

RUN yum install -y cronie python3

RUN pip3 install --upgrade pip

COPY systemctl3.py /usr/bin/systemctl3
RUN chmod a+x /usr/bin/systemctl3

COPY . /usr/src/app

RUN pip3 install -r /usr/src/app/requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:5000/memory || exit 1

ENTRYPOINT /usr/src/app/start.sh
