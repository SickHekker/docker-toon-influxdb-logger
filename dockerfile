FROM alpine

RUN apk update

RUN apk add --update python py-pip

RUN pip install influxdb

COPY toonlog.py /src/toonlog.py

COPY Toon.py /src/Toon.py

CMD python /src/toonlog.py
