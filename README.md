# docker-toon-influxdb-logger
logs the temperature recorded by toon to influxdb by connecting to the eneco servers and pulling the temperatures using Toon.py by rvdm
https://github.com/rvdm/toon

don't forget to put your information in the toonlog.py file for the influxdb server and eneco login

then do:
sudo docker build -t toonlog .
