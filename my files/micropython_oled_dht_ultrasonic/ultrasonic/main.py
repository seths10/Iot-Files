from hcsr04 import HCSR04
from machine import Pin,I2C
import ssd1306,time

i2c = I2C(scl=Pin(22), sda=Pin(21))      #Init i2c
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3c) 

sensor = HCSR04(trigger_pin=5, echo_pin=18,echo_timeout_us=1000000)

while True:
    distance = sensor.distance_cm()
    print(distance,' cm')
    time.sleep_ms(100)
    oled.fill(0)
    oled.text("Distance:",30,20) 
    oled.text(str(distance),30,40)
    oled.text("cm",30,50)
    oled.show()
    








