FROM centos:7

RUN yum update -y 
RUN  yum install -y python36 python36-devel python36-setuptools

RUN pip3 install flask 

EXPOSE 5000

COPY app.py /var/app/app.py

WORKDIR /var/app

CMD python3 app.py

