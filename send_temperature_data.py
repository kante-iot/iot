import requests
import json
import logging
import datetime

# TODO : 이곳 변경
device_id = 1
building_name = "twosun"
floor = 5

import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# TODO : 서버 구축되면 변경
url = f"http://smartoffice.kakaoent.cc:8080/api/sensor-data"

data = {
    "humidity": int(humidity),
    "temperature": int(temperature),
    "device" : device_id
}
response = requests.post(url, data=data)

# Logging
d = datetime.datetime.now()
logging.basicConfig(
    filename=f"{d.year}-{d.month}-{d.day}.log",
    level= logging.INFO,
    format='%(asctime)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)

if response.status_code == 200:
    logging.info(f"SUCCESS, humidity : {humidity}, temperature : {temperature}")
else:
    logging.info(f"FAIL, humidity : {humidity}, temperature : {temperature}")
