FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get -y install tzdata
RUN apt-get install -y libreoffice

WORKDIR /app

RUN mkdir result
COPY template/* template/
COPY reqirement.txt .
RUN pip3 install -r reqirement.txt
COPY util.py .
COPY word-pdf.py .

ENTRYPOINT [ "python3",  "word-pdf.py" ]
CMD []
