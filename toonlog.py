from Toon import Toon
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import time
import sys


toonusername = "YOURTOONUSERNAME"
toonpassword = "YOURTOONPASSWORD"

toon = Toon(toonusername,toonpassword)

client = InfluxDBClient('address', port, 'user', 'password', 'database')

def save_data(sensor):
	toon.login()
   	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    	thermostat = toon.get_thermostat_info()
	powerstats = toon.get_power_usage()
	temperature = temp = float(thermostat["currentTemp"]) / 100
	power = = float(powerstats["powerUsage"]) / 100
	toon.logout()
	if temperature is not None:
        	print('Sensor={0}  Temp={1:0.1f}*C Power={0:0.1f}watts'.format(sensor, temperature, power))
        	json_body = [
            	{
                	"measurement": "toon",
                	"timestamp": current_time,
                	"fields": {
                    	    "temperature": float("{0:0.1f}".format(temperature))
			    "power": float("{0:0.1f}".format(power))
			}
           	 }]
        	# print(json_body) #for debug, not enabled
        	client.write_points(json_body)
		
		

while True:
	try:
		save_data('toon')
		time.sleep(30) 
	except KeyboardInterrupt:
   		sys.exit()
        
