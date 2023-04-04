FROM centos:7

MAINTAINER AlexU <master0000222@gmail.com>

ENV TZ=Europe/Moscow

COPY . /task/

RUN yum update -y && yum install -y python3

WORKDIR /task/

EXPOSE 5000

RUN pip3 install flask-restful

CMD ["python3", "app.py"]

