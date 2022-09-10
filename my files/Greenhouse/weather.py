from machine import Pin, Timer, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import network
import time
from umqtt.robust import MQTTClient
import sys
import dht
from servo import Servo

dht = dht.DHT11(Pin(33))
pump = Pin(27, Pin.OUT)
led = Pin(4,Pin.OUT)
fan = Pin(2, Pin.OUT)



I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16

pump.value(0)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


WIFI_SSID     = 'iotdevlab+virus'
WIFI_PASSWORD = 'm,./@1234'

mqtt_client_id      = bytes('client_'+'12321', 'utf-8')

ADAFRUIT_IO_URL     = 'io.adafruit.com' 
ADAFRUIT_USERNAME   = 'seths10'
ADAFRUIT_IO_KEY     = 'aio_ymIO65YSI2mBqjdIh0BVPCemXEGP'

LED_FEED_ID      = 'led'
TEMP_FEED_ID      = 'temp'
HUM_FEED_ID      = 'hum'

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect(WIFI_SSID,WIFI_PASSWORD)
    if not wifi.isconnected():
        print('connecting..')
        lcd.putstr("Connecting...")
        lcd.clear()
        timeout = 0
        while (not wifi.isconnected() and timeout < 10):
            print(10 - timeout)
            timeout = timeout + 1
            time.sleep(1) 
    if(wifi.isconnected()):
        print('connected')
        lcd.putstr("Connected")
        lcd.clear()
    else:
        print('not connected')
        sys.exit()
        

connect_wifi()

client = MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)
try:            
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()
    

def callback(topic, message):
    print('Received Data:  Topic = {}, Message = {}'.format(topic, message))
    recieved_data = str(message,'utf-8')
    if recieved_data=="0":
        led.value(0)
    if recieved_data=="1":
        led.value(1)
        
temp_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, TEMP_FEED_ID), 'utf-8')
hum_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, HUM_FEED_ID), 'utf-8')  
toggle_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, LED_FEED_ID), 'utf-8')


client.set_callback(callback)
client.subscribe(toggle_feed)

def pump_light(data1):
    pump.value(1)
    time.sleep(1)
    pump.value(0)
    
    if led.value() == 1:
        led.value(0)
    else:
        led.value(1)

def sens_data(data):
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
    
    client.publish(temp_feed,    
                  bytes(str(temp), 'utf-8'),
                  qos=0)
    
    client.publish(hum_feed,    
                  bytes(str(hum), 'utf-8'),
                  qos=0)
    print("Temperature: ", str(temp))
    print("Humudity: " , str(hum))
    print('Readings Sent')
        
    
    lcd.putstr("Temperature: ")
    lcd.putstr(str(temp))
    lcd.move_to(0,1)
    lcd.putstr("Humidity: ")
    lcd.putstr(str(hum))
    lcd.clear()
    
     
    if temp > 30:
        s =  Servo(25)
        s.angle(0)
        time.sleep(10)
        s.angle(100)           
#     else:
#         sens_data()

push_data = Timer(0)
push_data.init(period=5000, mode=Timer.PERIODIC, callback = sens_data)

pump_and_light = Timer(33)
pump_and_light.init(period=10800000, mode=Timer.PERIODIC, callback = pump_light)


while True:
    try:
        client.check_msg()
    except :
        client.disconnect()
        sys.exit()    