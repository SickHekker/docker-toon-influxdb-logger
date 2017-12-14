# docker-toon-influxdb-logger
logs the temperature recorded by toon to influxdb by connecting to the eneco servers and pulling the temperatures using Toon.py by rvdm
https://github.com/rvdm/toon



cd docker-toon-influxdb-logger

put your information in the toonlog.py file for the influxdb server and eneco login

docker build -t toonlog .

docker run --name=toonlog toonlog

