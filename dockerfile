FROM alpine

RUN apk update

RUN apk add --update python py-pip

RUN pip install influxdb

RUN COPY toonlog.py /src/toonlog.py

RUN COPY Toon.py /src/Toon.py
