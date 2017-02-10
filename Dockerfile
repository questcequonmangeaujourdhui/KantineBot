FROM debian:latest

RUN apt-get update && apt-get install -y locales locales-all python3 python3-pip python3-requests && rm -rf /var/lib/apt/lists/*

RUN pip3 install telepot

ADD kantineBot.py /opt/

ENV TZ=Europe/Paris
ENV LC_ALL=en_US.UTF-8

ENTRYPOINT [ "/opt/kantineBot.py" ]
