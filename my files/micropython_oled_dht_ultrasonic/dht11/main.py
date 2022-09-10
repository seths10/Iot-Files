from machine import Pin
from machine import Pin,I2C
import ssd1306
import dht    
import time

i2c = I2C(scl=Pin(22), sda=Pin(21))      #Init i2c
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3c) 

p15=Pin(15, Pin.IN)
d=dht.DHT11(p15)           

while True:
    d.measure()       #Measurement of temperature and humidity
    t=d.temperature() #Read Celsius temperature
    h=d.humidity()    #Read relative humidity
    print('Temperature=', t, 'C', 'Humidity=', h, '%')
    time.sleep(1)                #Delay of 1 second
    oled.fill(0)
    oled.text("Temperature^C",10,10)
    oled.text(str(t),80,20)
    oled.text("Humidity  %",10,40)
    oled.text(str(h),80,55)
    oled.show()


    
