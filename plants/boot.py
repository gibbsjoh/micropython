# Complete project details at https://RandomNerdTutorials.com
from time import sleep

try:
  import usocket as socket
except:
  import socket

from machine import Pin, ADC
import network

useCSV = 1

if useCSV == 1:

  # If we have multiple sensors (or just 1 for now), read in a list of sensor names & pins from a CSV file
  sensorPins = []
  delim = ','
  with open('pins.csv','r') as file:
    for line in file:
      line = line.replace('"', '')
      sensorPins.append(line.rstrip('\n').rstrip('\r').split(delim))

  # parse the sensorPins dictionary to create the different sensors
  # how many entries in the dictionary:
  theLength = len(sensorPins)
  i = 0
  for sensors in sensorPins:
    varName = sensorPins[i]
    pinNumber = sensorPins[i][1]
    globals()[varName] = ADC(Pin(pinNumber))
    globals()[varName].atten(ADC.ATTN_11DB)       #Full range: 3.3v

else:
  plant01 = ADC(Pin(34))
  plant01.atten(ADC.ATTN_11DB)  # Full range: 3.3v

import esp
esp.osdebug(None)

import gc
gc.collect()

led = Pin(2, Pin.OUT)
led.value(0)

ssid = 'iot_wlan'
password = 'Motorola68040'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  print('Connecting...')
  pass

print('Connection successful')
print(station.ifconfig())
led.value(1)
sleep(2)
led.value(0)

# while True:
#   plant01_value = plant01.read()
#   print(plant01_value)
#   sleep(0.1)