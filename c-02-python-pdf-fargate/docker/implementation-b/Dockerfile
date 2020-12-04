FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y


# RUN apt-get install -y python3
# RUN apt-get install -y python3-pip
# RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get -y install tzdata
# RUN apt-get install -y libreoffice
# RUN apt-get install -y abiword

# RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get -y install tzdata

RUN apt-get install -y wget
RUN wget https://packages.microsoft.com/config/ubuntu/20.10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libgdiplus
RUN apt-get install -y dotnet-runtime-5.0
# RUN apt-get install -y python3
# RUN apt-get install -y python3-pip

WORKDIR /app

RUN mkdir result
COPY word-pdf/publish/* publish/

# COPY reqirement.txt .
# RUN pip3 install -r reqirement.txt

# COPY template/* template/
# COPY testdata.py .
# COPY util.py .
# COPY word-pdf.py .

ENTRYPOINT [ "./publish/word-pdf",  "" ]
CMD []
