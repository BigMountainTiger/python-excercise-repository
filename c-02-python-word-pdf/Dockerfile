FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libreoffice

WORKDIR /app

ENTRYPOINT [ "which",  "libreoffice" ]
CMD []
