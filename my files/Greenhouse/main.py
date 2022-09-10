from machine import Pin, Timer
import network
import time
from umqtt.robust import MQTTClient
import sys
import dht
from pump import *

led = Pin(4,Pin.OUT)
fan = Pin(2, Pin.OUT)

soil_moisture = 10

# WIFI_SSID     = 'iotdevlab+virus'
# WIFI_PASSWORD = 'm,./@1234'
# 
# mqtt_client_id      = bytes('client_'+'12321', 'utf-8')
# 
# ADAFRUIT_IO_URL     = 'io.adafruit.com' 
# ADAFRUIT_USERNAME   = 'seths10'
# ADAFRUIT_IO_KEY     = 'aio_ymIO65YSI2mBqjdIh0BVPCemXEGP'
# 
# LED_FEED_ID      = 'led'
# TEMP_FEED_ID      = 'temp'
# HUM_FEED_ID      = 'hum'
# 
# def connect_wifi():
#     wifi = network.WLAN(network.STA_IF)
#     wifi.active(True)
#     wifi.disconnect()
#     wifi.connect(WIFI_SSID,WIFI_PASSWORD)
#     if not wifi.isconnected():
#         print('connecting..')
#         timeout = 0
#         while (not wifi.isconnected() and timeout < 10):
#             print(10 - timeout)
#             timeout = timeout + 1
#             time.sleep(1) 
#     if(wifi.isconnected()):
#         print('connected')
#     else:
#         print('not connected')
#         sys.exit()
#         
# 
# connect_wifi()
# 
# client = MQTTClient(client_id=mqtt_client_id, 
#                     server=ADAFRUIT_IO_URL, 
#                     user=ADAFRUIT_USERNAME, 
#                     password=ADAFRUIT_IO_KEY,
#                     ssl=False)
# try:            
#     client.connect()
# except Exception as e:
#     print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
#     sys.exit()
# 
# def callback(topic, message):
#     print('Received Data:  Topic = {}, Message = {}'.format(topic, message))
#     recieved_data = str(message,'utf-8')
#     if recieved_data=="0":
#         led.value(0)
#     if recieved_data=="1":
#         led.value(1)
#         
# temp_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, TEMP_FEED_ID), 'utf-8')
# hum_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, HUM_FEED_ID), 'utf-8')  
# toggle_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, LED_FEED_ID), 'utf-8')
# 
# 
# client.set_callback(callback)
# client.subscribe(toggle_feed)


def sens_data(data):
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
#     client.publish(temp_feed,    
#                   bytes(str(temp), 'utf-8'),
#                   qos=0)
#     
#     client.publish(hum_feed,    
#                   bytes(str(hum), 'utf-8'),
#                   qos=0)
    temp_measure()
    displaytemp()
    
    if soil_moisture < 10:
        pump_water()

timer = Timer(0)
timer.init(period=5000, mode=Timer.PERIODIC, callback = sens_data)

# while True:
#     try:
#         client.check_msg()
#     except :
#         client.disconnect()
#         sys.exit()