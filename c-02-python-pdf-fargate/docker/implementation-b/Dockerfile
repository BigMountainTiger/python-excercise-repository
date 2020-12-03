FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get -y install tzdata
# RUN apt-get install -y libreoffice
RUN apt-get install -y abiword

WORKDIR /app

COPY reqirement.txt .
RUN pip3 install -r reqirement.txt

RUN mkdir result
COPY template/* template/
COPY testdata.py .
COPY util.py .
COPY word-pdf.py .

ENTRYPOINT [ "python3",  "word-pdf.py" ]
CMD []
