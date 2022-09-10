from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import dht
import time

dht = dht.DHT11(Pin(33))

I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16

dht.measure()
temp = dht.temperature()
hum = dht.humidity()

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

#     lcd.putstr("Automated Greenhouse")
#     time.sleep(5)
#     lcd.clear()
def displaytemp():
    lcd.putstr("Temperature: ")
    lcd.putstr(str(temp))
    lcd.move_to(0,1)
    lcd.putstr("Humidity: ")
    lcd.putstr(str(hum))
    time.sleep(5)
    lcd.clear()