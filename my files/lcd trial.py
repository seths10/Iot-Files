import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import dht

d = dht.DHT11(Pin(33))

I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)



# heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])
# face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])
# lcd.custom_char(0, heart)
# lcd.custom_char(1, face)
# lcd.putstr(chr(0)+" ESP32 with I2C LCD "+chr(1))


while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    lcd.putstr("Automated Greenhouse")
    sleep(5)
    lcd.clear()
    lcd.putstr("Temperature: ")
    lcd.putstr(str(temp))
    lcd.move_to(0,1)
    lcd.putstr("Humidity: ")
    lcd.putstr(str(hum))
    sleep(10)
    lcd.clear()
